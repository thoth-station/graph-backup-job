#!/usr/bin/env python3
# Graph Backup Job
# Copyright(C) 2019, 2020 Harshad Reddy Nalla, Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Graph backup logic for the Thoth project."""

import logging
import os
from thoth.analyzer import run_command
from thoth.common import init_logging
from thoth.storages import __version__ as __storages__version__
from thoth.storages import GraphBackupStore, GraphDatabase

from prometheus_client import Gauge, CollectorRegistry, push_to_gateway


init_logging()
_LOGGER = logging.getLogger("thoth.graph_backup_job")
__version__ = "0.10.0"
__component_version__ = f"{__version__}+thoth_storage.{__storages__version__}"
COMPONENT_NAME = "graph-backup-job"

THOTH_DATA_DUMP_PATH = os.getenv("THOTH_DATA_DUMP_PATH", "pg_dump.sql")

KNOWLEDGE_GRAPH_HOST = os.getenv("KNOWLEDGE_GRAPH_HOST", "localhost")
KNOWLEDGE_GRAPH_PORT = os.getenv("KNOWLEDGE_GRAPH_PORT", "5432")
KNOWLEDGE_GRAPH_USER = os.getenv("KNOWLEDGE_GRAPH_USER", "postgres")
KNOWLEDGE_GRAPH_DATABASE = os.getenv("KNOWLEDGE_GRAPH_DATABASE", "postgres")

# metrics
THOTH_METRICS_PUSHGATEWAY_URL = os.getenv("PROMETHEUS_PUSHGATEWAY_URL")
THOTH_DEPLOYMENT_NAME = os.getenv("THOTH_DEPLOYMENT_NAME")

prometheus_registry = CollectorRegistry()

database_schema_revision_script = Gauge(
    "thoth_database_schema_revision_script",
    "Thoth database schema revision from script",
    ["component", "revision", "env"],
    registry=prometheus_registry,
)

_METRIC_PG_DUMP_STATUS = Gauge(
    "thoth_graph_backup_job",
    "Thoth Graph Backup Job save status",
    ["env", "version"],
    registry=prometheus_registry,
)


def _send_metrics():
    """Send metrics to pushgateway."""
    if THOTH_METRICS_PUSHGATEWAY_URL and THOTH_DEPLOYMENT_NAME:
        try:
            _LOGGER.debug(f"Submitting metrics to Prometheus pushgateway {THOTH_METRICS_PUSHGATEWAY_URL}")
            push_to_gateway(
                THOTH_METRICS_PUSHGATEWAY_URL,
                job=COMPONENT_NAME,
                registry=prometheus_registry,
            )
        except Exception as e:
            _LOGGER.exception(f"An error occurred pushing the metrics: {str(e)}")

    else:
        _LOGGER.warning("PROMETHEUS_PUSHGATEWAY_URL env variable is not set.")


def main():
    """Perform graph backup job."""
    _LOGGER.debug("Debug mode is on.")

    if THOTH_DEPLOYMENT_NAME:
        database_schema_revision_script.labels(
            COMPONENT_NAME, GraphDatabase().get_script_alembic_version_head(), THOTH_DEPLOYMENT_NAME
        ).inc()
    else:
        _LOGGER.warning("THOTH_DEPLOYMENT_NAME env variable is not set.")

    adapter = GraphBackupStore()
    adapter.connect()

    _LOGGER.info("Starting creation of the database dump")
    try:
        run_command(
            f"pg_dump -h {KNOWLEDGE_GRAPH_HOST} -p {KNOWLEDGE_GRAPH_PORT} "
            f"-U {KNOWLEDGE_GRAPH_USER} -d {KNOWLEDGE_GRAPH_DATABASE} -f {THOTH_DATA_DUMP_PATH}",
            env={"PGPASSWORD": os.getenv("KNOWLEDGE_GRAPH_PASSWORD", "postgres")},
            timeout=None,
        )
        _LOGGER.info("Uploading the database dump")

        object_id = adapter.store_dump(f"{THOTH_DATA_DUMP_PATH}")
        _LOGGER.info("The database dump is available at %s/%s", adapter.prefix, object_id)
        _LOGGER.info("Graph backup task is done.")

        _METRIC_PG_DUMP_STATUS.labels(THOTH_DEPLOYMENT_NAME, __component_version__).set(0)

    except Exception as e:
        _METRIC_PG_DUMP_STATUS.labels(THOTH_DEPLOYMENT_NAME, __component_version__).set(1)
        _LOGGER.exception(f"Error saving the pg dump {e}.")
    finally:
        _send_metrics()


if __name__ == "__main__":
    _LOGGER.info("graph-backup-job v%s starting...", __component_version__)
    main()
