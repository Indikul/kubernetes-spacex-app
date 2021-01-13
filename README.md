# kubernetes-spacex-app
This is a micro service based mock application using Kubernetes on minikube

This is a flaks app. You can give some string values in some boxes given,data will get saved in a mysql db and show in a table.

1. First create two custom docker images.

Docker images 1. indikul/cw_app
              2. indikul/custom_mysql
              
2. Then create pods, services and deployment files and deploy the app in minikube kubernetes.
