#! /bin/bash
docker build . -t test1 -f Dockerfile
aws ecr get-login-password --region "us-west-2" |sudo docker login --username AWS --password-stdin 683632682714.dkr.ecr.us-west-2.amazonaws.com
docker tag test1 683632682714.dkr.ecr.us-west-2.amazonaws.com/cim-airflow-demo:cipio-test
docker push 683632682714.dkr.ecr.us-west-2.amazonaws.com/cim-airflow-demo:cipio-test
