#!/usr/bin/env python3
# Graph Backup Job
# Copyright(C) 2019 Harshad Reddy Nalla, Fridolin Pokorny
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
from thoth.storages import GraphBackupStore

init_logging()
_LOGGER = logging.getLogger("thoth.graph_backup_job")
__version__ = f"0.6.0+thoth_storage.{__storages__version__}"
KNOWLEDGE_GRAPH_HOST = os.getenv("KNOWLEDGE_GRAPH_HOST", "localhost")
KNOWLEDGE_GRAPH_PORT = os.getenv("KNOWLEDGE_GRAPH_PORT", "5432")
KNOWLEDGE_GRAPH_USER = os.getenv("KNOWLEDGE_GRAPH_USER", "postgres")
KNOWLEDGE_GRAPH_DATABASE = os.getenv("KNOWLEDGE_GRAPH_DATABASE", "postgres")


def main():
    """Perform graph backup job."""
    _LOGGER.debug("Debug mode is on.")
    adapter = GraphBackupStore()
    adapter.connect()

    _LOGGER.info("Starting creation of the database dump")
    run_command(
        f"pg_dump -h {KNOWLEDGE_GRAPH_HOST} -p {KNOWLEDGE_GRAPH_PORT} "
        f"-U {KNOWLEDGE_GRAPH_USER} -d {KNOWLEDGE_GRAPH_DATABASE} -f pg_dump.sql",
        env={"PGPASSWORD": os.getenv("KNOWLEDGE_GRAPH_PASSWORD", "postgres")},
        timeout=None,
    )
    _LOGGER.info("Uploading the database dump")
    object_id = adapter.store_dump("pg_dump.sql")
    _LOGGER.info("The database dump is available at %s/%s", adapter.prefix, object_id)
    _LOGGER.info("Graph backup task is done.")


if __name__ == "__main__":
    _LOGGER.info("graph-backup-job v%s starting...", __version__)
    main()
