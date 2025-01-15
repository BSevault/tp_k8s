<h1 align="center">
  <img src="https://github.com/cncf/artwork/blob/main/projects/kubernetes/icon/color/kubernetes-icon-color.png" alt="Kubernetes logo" width="50">
  TP K8s
</h1>

Installer minikube

Pour se mettre dans le docker de minikube dans un terminal:\
`eval $(minikube docker-env)`

Pour unset:\
`eval $(minikube docker-env -u)`

Pour voir où on est:\
`docker images`

Pour lister les contextes:\
`kubectl config get-contexts`

Pour chanegr de context:\
`kubectl config use-context minikube`

Pour démarrer minikube\
`minikube start`

Build Docker images depuis les repertoires où sont les fichiers Dockerfile\
`docker build -t frontend:v1 .`\
`docker build -t backend0:v1 .`\
`docker build -t backend1:v1 .`\
`docker build -t backend2:v1 .`

Pour appliquer les config kub:
- `kubectl apply -f backend-deployment.yaml`
- `kubectl apply -f frontend-deployment.yaml`
- `kubectl apply -f frontend-service.yaml`

Obtenir l'URL du frontend avec Minikube:\
`minikube service frontend-service --url`\
ou\
`minikube service frontend-svc --url`

Supprimer tous les pods\
`kubectl delete pods --all`

Supprimer tous les services sauf kubernetes\
`kubectl delete deployments --all`\
`kubectl delete pods --all`\
`kubectl delete svc --field-selector metadata.name!=kubernetes`