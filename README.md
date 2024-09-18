### 1. Basit bir jenkins-script.sh dosyasını localde çalıştırma.

```
kubectl get pods
```

```
kubectl cp ./jenkins-script.sh <jenkins-pod-name>:/var/jenkins_home/
```

```
kubectl exec -it <jenkins-pod-name> -- /bin/bash
```

```
sh /var/jenkins_home/jenkins-script.sh
```
### 2. Basit bir script.sh dosyasını jenkins browserda çalıştırma.

- Jenkins pod'una giriş yap:

```
kubectl exec -it <jenkins-pod-name> -- /bin/bash
```
- Çalıştırma İzni Verme

```
chmod +x /var/jenkins_home/jenkins-script.sh
```

### 3.