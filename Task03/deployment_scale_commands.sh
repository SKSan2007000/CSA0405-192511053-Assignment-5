#!/usr/bin/env bash
set -euo pipefail
kubectl apply -f ../Task02/deployment.yaml
kubectl get deployment,pods,svc -l app=result-portal
POD=$(kubectl get pods -l app=result-portal -o jsonpath='{.items[0].metadata.name}')
kubectl delete pod "$POD"
kubectl get pods -l app=result-portal -w
kubectl scale deployment/result-portal --replicas=6
kubectl get pods -l app=result-portal
