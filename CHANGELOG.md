
## Release 0.7.0 (2020-09-02T07:00:37)
### Features
* include the templates and maintainer
* :truck: include aicoe-ci configuration file
* :8ball: not all updates are required for postgresql10 (#118)
* Remove latest versions limitation (#115)
* :pushpin: Automatic dependency re-locking (#109)
* Create OWNERS
* added a 'tekton trigger tag_release pipeline issue'
* Remove latest version restriction from .thoth.yaml
* Increase memory requirements doe to OOM
* Update .thoth.yaml
* Update .thoth.yaml
* Update .thoth.yaml
* Use PostgreSQL 10
* Do not run testsuite as there is nothing to run
* Happy new year!
* Set starting deadline seconds to null
* Use new dump logic that rotates files stored
* Simplify backup handling
* :package: thothTemplate required for thoth advise
* :star: thoth-s2i based dockerfile for postgresql
* Add liveness probe
* Do not use timeout on run_command
* Add missing import
* :construction_worker: application to take backup of db and store to ceph
* :package: openshift template to deploy the cronjob
* :nut_and_bolt: github templates for issues and pr
* :zap: support from Thoth sourceops services
### Bug Fixes
* Fallback to Pipfile.lock present in the repo on any Thoth error
* Be consistent with the rest of the repos
### Improvements
* Split version and component version (#129)
* Remove OpenShift templates, use Thoth application (#113)
* Increase memory and CPU requirements
* Do not run adviser from bc in debug mode
* No need to have special SA for this cronjob
* :books: updated README.md
* Remove unused variable
### Automatic Updates
* :pushpin: Automatic update of dependency thoth-common from 0.15.0 to 0.17.2 (#131)
* :pushpin: Automatic update of dependency thoth-storages from 0.24.5 to 0.25.5 (#127)
* :pushpin: Automatic update of dependency thoth-common from 0.14.2 to 0.15.0 (#123)
* :pushpin: Automatic update of dependency thoth-common from 0.14.2 to 0.15.0 (#122)
* :pushpin: Automatic update of dependency thoth-storages from 0.24.4 to 0.24.5 (#121)
* :pushpin: Automatic update of dependency thoth-storages from 0.24.4 to 0.24.5 (#120)
* :pushpin: Automatic update of dependency thoth-common from 0.14.1 to 0.14.2 (#117)
* :pushpin: Automatic update of dependency thoth-storages from 0.24.2 to 0.24.4 (#116)
* :pushpin: Automatic update of dependency thoth-storages from 0.24.0 to 0.24.2 (#114)
* :pushpin: Automatic update of dependency thoth-common from 0.13.3 to 0.14.1 (#112)
* :pushpin: Automatic update of dependency thoth-common from 0.13.3 to 0.14.1 (#111)
* :pushpin: Automatic update of dependency thoth-storages from 0.22.9 to 0.24.0 (#110)
* :pushpin: Automatic update of dependency thoth-common from 0.13.1 to 0.13.2
* :pushpin: Automatic update of dependency thoth-storages from 0.22.8 to 0.22.9
* :pushpin: Automatic update of dependency thoth-common from 0.13.0 to 0.13.1
* :pushpin: Automatic update of dependency thoth-storages from 0.22.7 to 0.22.8
* :pushpin: Automatic update of dependency thoth-common from 0.12.10 to 0.13.0
* :pushpin: Automatic update of dependency thoth-common from 0.12.9 to 0.12.10
* :pushpin: Automatic update of dependency thoth-common from 0.12.8 to 0.12.9
* :pushpin: Automatic update of dependency thoth-common from 0.12.7 to 0.12.8
* :pushpin: Automatic update of dependency thoth-common from 0.12.6 to 0.12.7
* :pushpin: Automatic update of dependency thoth-common from 0.12.5 to 0.12.6
* :pushpin: Automatic update of dependency thoth-common from 0.12.4 to 0.12.5
* :pushpin: Automatic update of dependency thoth-storages from 0.22.6 to 0.22.7
* :pushpin: Automatic update of dependency thoth-storages from 0.22.5 to 0.22.6
* :pushpin: Automatic update of dependency thoth-common from 0.12.3 to 0.12.4
* :pushpin: Automatic update of dependency thoth-common from 0.12.1 to 0.12.3
* :pushpin: Automatic update of dependency thoth-common from 0.12.0 to 0.12.1
* :pushpin: Automatic update of dependency thoth-common from 0.10.12 to 0.12.0
* :pushpin: Automatic update of dependency thoth-storages from 0.22.3 to 0.22.5
* :pushpin: Automatic update of dependency thoth-common from 0.10.11 to 0.10.12
* :pushpin: Automatic update of dependency thoth-common from 0.10.9 to 0.10.11
* :pushpin: Automatic update of dependency thoth-common from 0.10.8 to 0.10.9
* :pushpin: Automatic update of dependency thoth-storages from 0.22.2 to 0.22.3
* :pushpin: Automatic update of dependency thoth-common from 0.10.7 to 0.10.8
* :pushpin: Automatic update of dependency thoth-common from 0.10.6 to 0.10.7
* :pushpin: Automatic update of dependency thoth-storages from 0.22.1 to 0.22.2
* :pushpin: Automatic update of dependency thoth-common from 0.10.5 to 0.10.6
* :pushpin: Automatic update of dependency thoth-storages from 0.22.0 to 0.22.1
* :pushpin: Automatic update of dependency thoth-storages from 0.21.11 to 0.22.0
* :pushpin: Automatic update of dependency thoth-common from 0.10.4 to 0.10.5
* :pushpin: Automatic update of dependency thoth-common from 0.10.3 to 0.10.4
* :pushpin: Automatic update of dependency thoth-common from 0.10.2 to 0.10.3
* :pushpin: Automatic update of dependency thoth-common from 0.10.1 to 0.10.2
* :pushpin: Automatic update of dependency thoth-common from 0.10.0 to 0.10.1
* :pushpin: Automatic update of dependency thoth-common from 0.9.31 to 0.10.0
* :pushpin: Automatic update of dependency thoth-common from 0.9.29 to 0.9.31
* :pushpin: Automatic update of dependency thoth-storages from 0.21.10 to 0.21.11
* :pushpin: Automatic update of dependency thoth-storages from 0.21.9 to 0.21.10
* :pushpin: Automatic update of dependency thoth-storages from 0.21.8 to 0.21.9
* :pushpin: Automatic update of dependency thoth-common from 0.9.28 to 0.9.29
* :pushpin: Automatic update of dependency thoth-storages from 0.21.7 to 0.21.8
* :pushpin: Automatic update of dependency thoth-common from 0.9.27 to 0.9.28
* :pushpin: Automatic update of dependency thoth-common from 0.9.26 to 0.9.27
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.7 to 0.1.8
* :pushpin: Automatic update of dependency thoth-storages from 0.21.6 to 0.21.7
* :pushpin: Automatic update of dependency thoth-common from 0.9.25 to 0.9.26
* :pushpin: Automatic update of dependency thoth-storages from 0.21.5 to 0.21.6
* :pushpin: Automatic update of dependency thoth-common from 0.9.24 to 0.9.25
* :pushpin: Automatic update of dependency thoth-storages from 0.21.4 to 0.21.5
* :pushpin: Automatic update of dependency thoth-storages from 0.21.3 to 0.21.4
* :pushpin: Automatic update of dependency thoth-storages from 0.21.2 to 0.21.3
* :pushpin: Automatic update of dependency thoth-storages from 0.21.1 to 0.21.2
* :pushpin: Automatic update of dependency thoth-common from 0.9.23 to 0.9.24
* :pushpin: Automatic update of dependency thoth-storages from 0.21.0 to 0.21.1
* :pushpin: Automatic update of dependency thoth-storages from 0.20.6 to 0.21.0
* :pushpin: Automatic update of dependency thoth-storages from 0.20.5 to 0.20.6
* :pushpin: Automatic update of dependency thoth-common from 0.9.22 to 0.9.23
* :pushpin: Automatic update of dependency thoth-storages from 0.20.4 to 0.20.5
* :pushpin: Automatic update of dependency thoth-storages from 0.20.3 to 0.20.4
* :pushpin: Automatic update of dependency thoth-storages from 0.20.2 to 0.20.3
* :pushpin: Automatic update of dependency thoth-storages from 0.19.30 to 0.20.2
* :pushpin: Automatic update of dependency thoth-storages from 0.19.27 to 0.19.30
* :pushpin: Automatic update of dependency thoth-common from 0.9.21 to 0.9.22
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.6 to 0.1.7
* :pushpin: Automatic update of dependency thoth-storages from 0.19.25 to 0.19.27
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.5 to 0.1.6
* :pushpin: Automatic update of dependency thoth-common from 0.9.20 to 0.9.21
* :pushpin: Automatic update of dependency thoth-common from 0.9.19 to 0.9.20
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.4 to 0.1.5
* :pushpin: Automatic update of dependency thoth-common from 0.9.16 to 0.9.19
* :pushpin: Automatic update of dependency thoth-storages from 0.19.24 to 0.19.25
* :pushpin: Automatic update of dependency thoth-analyzer from 0.1.4 to 0.1.5

## Release 0.8.0 (2021-02-01T07:38:46)
### Features
* Introduce revision metrics (#136)
* port to python 38 (#133)
* py38 based on image for graph-backup (#134)

## Release 0.8.1 (2021-02-25T14:23:17)
### Features
* :arrow_up: Automatic update of dependencies by Kebechet (#142)
* :arrow_up: Automatic update of dependencies by Kebechet (#141)
* kebechet issue templates for ease trigger
