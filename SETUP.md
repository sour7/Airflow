1. Ref: https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
2.  dwonload yml file for windows: curl -LfO https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml


## Airflow Docker Install Python Package
 - add package in requirements.txt
 - extend docker image as done in `dockerfile.`
 - run `docker build . --tag extending_airflow:latest`