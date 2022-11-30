#!/bin/sh

docker build -t my_flask .

kubectl create secret generic regcred \
    --from-file=.dockerconfigjson=/home/usko/.docker/config.json> \
    --type=kubernetes.io/dockerconfigjson