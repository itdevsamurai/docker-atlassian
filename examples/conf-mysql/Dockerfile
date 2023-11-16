FROM ghcr.io/itdevsamurai/docker-atlassian:conf-8.6.1
ARG MYSQL_CONNECTOR_VERSION=8.0.32
ADD https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-j-${MYSQL_CONNECTOR_VERSION}.tar.gz /opt/atlassian/confluence/lib
RUN tar xf /opt/atlassian/confluence/lib/mysql-connector-j-${MYSQL_CONNECTOR_VERSION}.tar.gz -C /opt/atlassian/confluence/lib \
    && mv /opt/atlassian/confluence/lib/mysql-connector-j-${MYSQL_CONNECTOR_VERSION}/mysql-connector-j-${MYSQL_CONNECTOR_VERSION}.jar /opt/atlassian/confluence/lib \
    && rm /opt/atlassian/confluence/lib/mysql-connector-j-${MYSQL_CONNECTOR_VERSION}.tar.gz \
    && rm -rf /opt/atlassian/confluence/lib/mysql-connector-j-${MYSQL_CONNECTOR_VERSION}
