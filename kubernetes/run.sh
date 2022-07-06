#!/bin/bash

kubectl delete -f library/library-secret.yaml
kubectl delete -f library/library-configmap.yaml
kubectl delete -f library/library-deployment.yaml
kubectl delete -f library/library-service.yaml
# kubectl delete -f library/library-ingress.yaml

kubectl delete -f shop/shop-secret.yaml
kubectl delete -f shop/shop-configmap.yaml
kubectl delete -f shop/shop-deployment.yaml
kubectl delete -f shop/shop-service.yaml
# kubectl delete -f shop/shop-ingress.yaml

kubectl delete -f user_management/user-secret.yaml
kubectl delete -f user_management/user-configmap.yaml
kubectl delete -f user_management/user-deployment.yaml
kubectl delete -f user_management/user-service.yaml
# kubectl delete -f user_management/user-ingress.yaml


kubectl delete pod --all
# kubectl delete pvc --all
# kubectl delete pv --all

# kubectl delete -f library/library-pv.yaml --all
# kubectl delete -f shop/shop-pv.yaml --all
# kubectl delete -f user/user-pv.yaml --all

kubectl apply -f library/library-pv.yaml
kubectl apply -f library/library-secret.yaml
kubectl apply -f library/library-configmap.yaml
kubectl apply -f library/library-deployment.yaml 
kubectl apply -f library/library-service.yaml
# kubectl apply -f library/library-ingress.yaml

kubectl apply -f shop/shop-pv.yaml
kubectl apply -f shop/shop-secret.yaml
kubectl apply -f shop/shop-configmap.yaml
kubectl apply -f shop/shop-deployment.yaml 
kubectl apply -f shop/shop-service.yaml
# kubectl apply -f shop/shop-ingress.yaml

kubectl apply -f user_management/user-pv.yaml
kubectl apply -f user_management/user-secret.yaml
kubectl apply -f user_management/user-configmap.yaml
kubectl apply -f user_management/user-deployment.yaml 
kubectl apply -f user_management/user-service.yaml
# kubectl apply -f user_management/user-ingress.yaml