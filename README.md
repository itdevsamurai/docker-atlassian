# docker-atlassian

Provides Dockerfile & configs to use Atlassian products on Docker for development purpose

This is a rebuild for [atlassian/jira-software](https://hub.docker.com/r/atlassian/jira-software)
to support `linux/arm64`.

## Supported platforms

* `linux/amd64`
* `linux/arm64`

## Usage

Pulling Jira 9.3.1 image: `docker pull ghcr.io/itdevsamurai/docker-atlassian:jira-9.3.1`

See all available tags here: [package tags](https://github.com/itdevsamurai/docker-atlassian/pkgs/container/docker-atlassian/versions?filters%5Bversion_type%5D=tagged)

To configure, refer [atlassian/jira-software](https://hub.docker.com/r/atlassian/jira-software)

## Examples

See [examples readme](examples/README.md).
