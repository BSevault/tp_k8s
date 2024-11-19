<p>
  <img src="https://github.com/cncf/artwork/blob/main/projects/kubernetes/icon/color/kubernetes-icon-color.png" alt="Kubernetes logo" style="width: 50px; vertical-align: middle; margin-right: 10px;">
  <h1>TP K8s</h1>
</p>

Installer minikube

Pour se mettre dans le docker de minikube dans un terminal:\
`eval $(minikube docker-env)`

Pour unset:\
`eval $(minikube docker-env -u)`

Pour voir où on est:\
`docker images`

Pour démarrer minikube\
`minikube start`

Pour appliquer les config kub:
- `kubectl apply -f backend-deployment.yaml`
- `kubectl apply -f frontend-deployment.yaml`
- `kubectl apply -f frontend-service.yaml`

Obtenir l'URL du frontend avec Minikube:\
`minikube service frontend-service --url`
