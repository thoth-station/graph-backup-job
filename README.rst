graph-backup-job
========

.. image:: https://img.shields.io/github/v/tag/thoth-station/graph-backup-job?style=plastic
  :target: https://github.com/thoth-station/graph-backup-job/tags
  :alt: GitHub tag (latest by date)

.. image:: https://quay.io/repository/thoth-station/graph-backup-job/status
  :target: https://quay.io/repository/thoth-station/graph-backup-job?tab=tags
  :alt: Quay - Build

A periodic cronjob to backup Thoth's knowledge graph

Base Images
-----------

graph-backup-job required image with postgresql10 pre-installed. we have created few base image for this purpose.

.. image:: https://quay.io/repository/thoth-station/s2i-thoth-ubi8-py38-postgres/status
  :target: https://quay.io/repository/thoth-station/s2i-thoth-ubi8-py38-postgres?tab=tags
  :alt: Quay - Build

Image based on the `python 3.8 <ubi8-py36-postgres/Dockerfile>`__

.. image:: https://quay.io/repository/thoth-station/s2i-thoth-ubi8-py36-postgres/status
  :target: https://quay.io/repository/thoth-station/s2i-thoth-ubi8-py36-postgres?tab=tags
  :alt: Quay - Build

Image based on the `python 3.6 <ubi8-py36-postgres/Dockerfile>`__
