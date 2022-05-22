# Musinsa
Musinsa_Test

## 1. 도커 이미지 pull 

docker pull tebily/11:musinsa_test_jonghwakim

## 2. K8S Pod 배포 

kubectl apply -f ./deployments.yaml --record

## 3. K8S Pod 상태 확인

kubectl get pods

## 4. K8S Pod 실행 및 접속 

kubectl exec --stdin --tty musinsa-deployment-[random value] -- /bin/bash

## 5. 파이썬 프로그램 실행

python3 AWS_IAM.py [파라미터 값]
