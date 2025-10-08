# demo-app-helm-chart
Demo Application Helm Chart

## Update Package

```bash
helm package charts/demo-app --destination docs/
helm repo index docs/ --url https://ruanbekker.github.io/demo-app-helm-chart
```
