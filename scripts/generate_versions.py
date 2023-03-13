import json

import requests

res = requests.get(
    "https://marketplace.atlassian.com/rest/2/products/key/jira-software/versions"
)
version_data = res.json()["_embedded"]["versions"]

versions = [ver["name"] for ver in version_data]

print(json.dumps(versions))
