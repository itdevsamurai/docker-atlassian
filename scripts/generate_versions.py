import json
from pathlib import Path

import requests

res = requests.get(
    "https://marketplace.atlassian.com/rest/2/products/key/jira-software/versions"
)
version_data = res.json()["_embedded"]["versions"]

versions = set([ver["name"] for ver in version_data])

with open(Path(__file__).parent.parent / "jira_versions.txt") as f:
    manual_versions = set()
    for line in f.readlines():
        manual_versions.add(line.strip())
versions.update(manual_versions)

print(json.dumps(sorted(versions)))
