import json
from pathlib import Path

import requests

res = requests.get(
    "https://marketplace.atlassian.com/rest/2/products/key/jira-software/versions"
)
version_data = res.json()["_embedded"]["versions"]

versions = set([ver["name"] for ver in version_data])

res = requests.get(
    "https://my.atlassian.com/download/feeds/eap/jira.json"
)
versions.update([json.loads(res.text[10:-1])[0]["version"]])

with open(Path(__file__).parent.parent / "jira_versions.txt") as f:
    manual_versions = set()
    for line in f.readlines():
        manual_versions.add(line.strip())
versions.update(manual_versions)

print(json.dumps(sorted(versions)))
