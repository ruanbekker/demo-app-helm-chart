#!/usr/bin/env bash

VERSION="$(yq -r '.appVersion' charts/demo-app/Chart.yaml)"
REPO="demo-app-helm-chart"

export DOCKER_BUILDKIT=0
docker build -t ruanbekker/${REPO}:${VERSION} .
docker tag ruanbekker/${REPO}:${VERSION} ruanbekker/${REPO}:latest
docker push ruanbekker/${REPO}:${VERSION}
docker push ruanbekker/${REPO}:latest

echo "ruanbekker/${REPO}:${VERSION} was pushed"
