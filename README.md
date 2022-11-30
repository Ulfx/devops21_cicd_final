- [Devops21 CICD Final](#devops21-cicd-final)
  - [How to install](#how-to-install)
  - [How to deploy](#how-to-deploy)
  - [How to run tests](#how-to-run-tests)
  - [Contributors](#contributors)



# Devops21 CICD Final

## How to install

Make sure you have docker, python and minikube installed.

cd into repo root and run `source ./scripts/main.sh`


## How to deploy

`echo <random password> > password.txt`
`echo <random user-password> > user-password.txt`

` kubectl create secret docker-registry regcred --docker-server=<server> --docker-username=<username> --docker-password=<password> --docker-email=<email>`

`kubectl create secret generic mysqldb-secrets --from-file=MYSQL_PASSWORD=./user-password.txt --from-file=MYSQL_ROOT_PASSWORD=./password.txt`

`kubectl apply -f pod_db.yaml`

`kubectl apply -f create_pod.yaml`

`kubectl expose pod flask-server-pod --selector "app=my_flask" --type=LoadBalancer --port=5000`

`minikube service flask-server-pod`



## How to run tests

run `pytest`
and `pytest --cov=shop_app tests`


## Contributors
* Usko
* Sanju
* Ulf

