# Deploying Prometheus and Grafana <https://medium.com/@gayatripawar401/deploy-prometheus-and-grafana-on-kubernetes-using-helm-5aa9d4fbae66>

```bash
helm search hub Prometheus
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/prometheus
```

The Prometheus PushGateway can be accessed via port 9091 on the following DNS name from within your cluster: prometheus-prometheus-pushgateway.default.svc.cluster.local

```bash
helm repo add grafana https://grafana.github.io/helm-charts 
helm repo update

helm install grafana grafana/grafana

kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```
add dashboard <https://github.com/ramdesh/flask-prometheus-grafana-example/blob/master/monitoring/grafana_dashboard.json>