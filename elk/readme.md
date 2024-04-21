# Let's setup  elk stack here

`helm repo add elastic https://helm.elastic.co` adding repo
`helm search repo elastic` check if output present
`helm repo update`

update values <https://medium.com/@davis.angwenyi/how-to-install-elastic-search-using-helm-into-kubernetes-de1fb1011076>
`helm show values elastic/filebeat > values.yml`

```bash
helm install elasticsearch elastic/elasticsearch -f values_elastic.yml 
helm install filebeat elastic/filebeat -f values_filebeat.yml 
helm install logstash elastic/logstash -f values_logstash.yml 
helm install kibana elastic/kibana -f values_kibana.yml 
```

```bash
kubectl get secret elasticsearch-master-credentials -o jsonpath="{.data.username}" | base64 --decode
kubectl get secret elasticsearch-master-credentials -o jsonpath="{.data.password}" | base64 --decode
```

popential kibana clean-up

```bash
kubectl delete configmap kibana-kibana-helm-scripts 
kubectl delete serviceaccount pre-install-kibana-kibana 
kubectl delete roles pre-install-kibana-kibana 
kubectl delete rolebindings pre-install-kibana-kibana 
kubectl delete job pre-install-kibana-kibana
```
