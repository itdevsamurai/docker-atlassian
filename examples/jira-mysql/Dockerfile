FROM ghcr.io/itdevsamurai/docker-atlassian:jira-9.6.0
ARG MYSQL_CONNECTOR_VERSION=8.0.32
ADD https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-j-${MYSQL_CONNECTOR_VERSION}.tar.gz /opt/atlassian/jira/lib
RUN tar xf /opt/atlassian/jira/lib/mysql-connector-j-${MYSQL_CONNECTOR_VERSION}.tar.gz -C /opt/atlassian/jira/lib \
    && mv /opt/atlassian/jira/lib/mysql-connector-j-${MYSQL_CONNECTOR_VERSION}/mysql-connector-j-${MYSQL_CONNECTOR_VERSION}.jar /opt/atlassian/jira/lib \
    && rm /opt/atlassian/jira/lib/mysql-connector-j-${MYSQL_CONNECTOR_VERSION}.tar.gz \
    && rm -rf /opt/atlassian/jira/lib/mysql-connector-j-${MYSQL_CONNECTOR_VERSION}
