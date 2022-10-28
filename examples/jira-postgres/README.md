# Jira & Postgres

## Usage

First time run: `make`

Then [fix permission issue](https://confluence.atlassian.com/jirakb/jira-server-throws-unable-to-create-directory-for-deployment-error-on-startup-389781040.html):

```shell
docker exec -it jira bash -c "mkdir -p /opt/atlassian/jira/conf/Catalina/localhost && chown -R 2001:2001 /opt/atlassian/jira/conf/Catalina/localhost"
```

Then restart the stack: `make stop-server && make`

* Run server: `make`
* Stop server: `make stop-server`
