minikube start --nodes 2 --driver=docker
alias kubectl="minikube kubectl --"

# Local Registry
minikube addons enable registry
docker run --rm -it --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:$(minikube ip):5000"
#docker run -dit -p 5000:5000 --name registry registry

# Push Images
docker tag cloud_fum_user_management localhost:5000/cloud_fum_user_management
docker push localhost:5000/cloud_fum_user_management

docker tag cloud_fum_library localhost:5000/cloud_fum_library
docker push localhost:5000/cloud_fum_library

docker tag mysql:5.7.22 localhost:5000/mysql:5.7.22
docker push localhost:5000/mysql:5.7.22


# User Management
kubectl create namespace user-management

kubectl apply -f mysql-secret.yaml --namespace=user-management
kubectl apply -f userdb-pvc.yaml --namespace=user-management
kubectl apply -f userdb-configmap.yaml --namespace=user-management
kubectl apply -f userdb-deployment.yaml --namespace=user-management
kubectl apply -f usermanagement-deployment.yaml --namespace=user-management


# Library
kubectl create namespace library

kubectl apply -f mysql-secret.yaml --namespace=library
kubectl apply -f librarydb-pvc.yaml --namespace=library
kubectl apply -f librarydb-configmap.yaml --namespace=library
kubectl apply -f librarydb-deployment.yaml --namespace=library
kubectl apply -f library-deployment.yaml --namespace=library


# ingress
minikube addons enable ingress
