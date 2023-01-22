# Get running k8 pods
```
kubectl get pods --field-selector=status.phase==Running
```

# Delete and recreate a pod
```
kubectl delete pod db-pod && kubectl create -f db_kube.yml
```

# Save image to tar to be used in microk8s
```
docker save k8app-backend-image:1.1 > k8app-backend-image.tar

```

# Restart deployments
```
kubectl rollout restart deployments.apps/db
kubectl rollout restart deployments.apps/frontend
kubectl rollout restart deployments.apps/backend
```

microk8s enable ingress:default-ssl-certificate=default/frontend-tls-secret