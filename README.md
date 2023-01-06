# Portfolio Site

This website will be a portfolio for people to view my achievements and my current projects.
It is currently being publicly hosted at: <https://atom.cs.house>

## Screenshots

![Front Page](/static/images/front-page.png)

## Building

For building this site, you will need Podman.

You can run by running:

1. `chmod a+x run_dev.sh`
2. `./run_dev.sh`

Or, manually:

1. `podman build -t dev`
2. `podman run -p 8080:8080 dev`

The website will be hosted on `localhost:8080`.
