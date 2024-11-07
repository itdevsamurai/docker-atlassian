# docker-atlassian

** NOTICE: Since Atlassian now supports `arm64`, we recommend you to use the official images from [Official Atlassian DockerHub](https://hub.docker.com/r/atlassian). The repo will be archived.**

Provides Dockerfile & configs to use Atlassian products on Docker for development purpose

This is a rebuild for [atlassian/jira-software](https://hub.docker.com/r/atlassian/jira-software)
to support `linux/arm64`.

## License

This repo is licensed under the [MIT License](LICENSE) for all files. The Atlassian product binaries are licensed under their respective licenses. Please do your own research if you plan on using these images.

## Supported platforms

* `linux/amd64`
* `linux/arm64`

## Usage

Pulling Jira 9.6.0 image: `docker pull ghcr.io/itdevsamurai/docker-atlassian:jira-9.6.0`

See all available tags here: [package tags](https://github.com/itdevsamurai/docker-atlassian/pkgs/container/docker-atlassian/versions?filters%5Bversion_type%5D=tagged)

To configure, refer [atlassian/jira-software](https://hub.docker.com/r/atlassian/jira-software)

## Add new version

If the version that you need is not available in the [package tags](https://github.com/itdevsamurai/docker-atlassian/pkgs/container/docker-atlassian/versions?filters%5Bversion_type%5D=tagged), you can add it by creating a PR.

For Jira, add the version that you need to `jira_versions.txt`, one version per line.

## Examples

See [examples readme](examples/README.md).
