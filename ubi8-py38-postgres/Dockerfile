FROM quay.io/thoth-station/s2i-thoth-ubi8-py38:latest
ENV LANG=en_US.UTF-8
USER 0
RUN yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm \
  && yum install -y --setopt=tsflags=nodocs postgresql10
USER 1001
