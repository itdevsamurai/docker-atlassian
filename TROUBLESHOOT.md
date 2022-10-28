# Troubleshooting

## Jira cannot connect to database

Sometimes Jira starts faster than the DB (DB needs to run startup scripts).

Simply restart the compose stack or `docker restart jira`.

## Unable to create directory for deployment

If Jira is unable to create folder `/opt/atlassian/jira/conf/Catalina/localhost` then
[fix permission issue](https://confluence.atlassian.com/jirakb/jira-server-throws-unable-to-create-directory-for-deployment-error-on-startup-389781040.html):

```shell
docker exec -it jira bash -c "mkdir -p /opt/atlassian/jira/conf/Catalina/localhost && chown -R 2001:2001 /opt/atlassian/jira/conf/Catalina/localhost"
```
