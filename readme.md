# TP K8s

install minikube

`eval $(minikube docker-env)` pour se mettre dans le docker de minikube dans un terminal

`eval $(minikube docker-env -u)` pour unset

`docker images` pour voir où on est

`minikube start` pour démarrer minikube

Pour appliquer les config kub:

- `kubectl apply -f backend-deployment.yaml`
- `kubectl apply -f frontend-deployment.yaml`
- `kubectl apply -f frontend-service.yaml`