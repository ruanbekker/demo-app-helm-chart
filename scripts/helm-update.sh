#!/usr/bin/env bash

helm package charts/demo-app --destination docs/
helm repo index docs/ --url https://ruanbekker.github.io/demo-app-helm-chart
