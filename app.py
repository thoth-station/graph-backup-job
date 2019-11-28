#!/usr/bin/env python3
# Graph Backup Job
# Copyright(C) 2019 Harshad Reddy Nalla.
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

import sys
import logging
import os
from datetime import datetime
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
os.environ["PGPASSWORD"] = os.getenv("KNOWLEDGE_GRAPH_PASSWORD", "postgres")


def store_backup_to_ceph(backup_file_dest: str, backup_file_name: str) -> str:
    """Upload the backup file to ceph."""
    adapter = GraphBackupStore()
    adapter.connect()
    document_id = adapter.store_file(backup_file_dest, backup_file_name)
    return document_id


def main():
    """Perform graph backup job."""
    _LOGGER.debug("Debug mode is on.")

    backup_file_name = f"pg_dump-{datetime.now().strftime('%s')}"
    _LOGGER.info("The database backup would be taken into: %r.", backup_file_name)
    backup_file_dest = os.path.abspath(backup_file_name)

    _LOGGER.info("Starting the subprocess to take the dump from database.")
    run_command(
        f"pg_dump -h {KNOWLEDGE_GRAPH_HOST} -p {KNOWLEDGE_GRAPH_PORT} -U {KNOWLEDGE_GRAPH_USER} -d {KNOWLEDGE_GRAPH_DATABASE} -f {backup_file_dest}"
    )
    _LOGGER.info("upload the database backup file to ceph storage.")
    try:
        document_id = store_backup_to_ceph(backup_file_dest, backup_file_name)
        _LOGGER.info("The database backup to document: %r, is complete in ceph.", document_id)
    except Exception as e:
        _LOGGER.exception("An error occurred while uploading backup to ceph: %r", str(e))
        sys.exit(1)

    _LOGGER.info("Graph backup task is done.")


if __name__ == "__main__":
    print(f"graph-backup-job v{__version__} starting...")
    main()
