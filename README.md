# demo-app-helm-chart
Demo Application Helm Chart

## Update Package

```bash
helm package charts/demo-app --destination docs/
helm repo index docs/ --url https://ruanbekker.github.io/demo-app-helm-chart
```

## Using this Repo

```bash
helm repo add demo-app https://ruanbekker.github.io/demo-app-helm-chart
helm search repo demo-app --versions
```

Outputs:

```bash
NAME                    CHART VERSION   APP VERSION     DESCRIPTION
demo-app/demo-app       0.1.0           1.16.0          A Helm chart for Kubernetes
```
