# Simple containerized application

This is a **TodoList application** which has **backend, frontend and database**.

## How to run:

### Docker

1) Go inside k8app folder
2) Run ```docker-compose up```
3) Navigate to **frontend** http://localhost:5000/
3) Navigate to **backend** http://localhost:8080/
4) Check out main page and visit http://localhost:8080/docs to play with API
5) If you wish you can connect to PostgresDB (find credentials in .env file) to investigate the items table and data
   stored in it

### Kubernetes

For learning purposes each of the team members created his own kubernetes YAML files that can be found in corresponding
branches

#### Microk8s (k8s-specs) folder

Requirements:

- [Minikube](https://minikube.sigs.k8s.io/docs/start/)

Start minikube

```bash
minikube start
```

Build image in minikube docker environment

```bash
eval $(minikube docker-env)

docker buildx build backend/ --platform=linux/amd64 -t k8app-backend-image:1.1
```

Run kubernetes specs

```bash
kubectl apply -f k8-specs
```

Expose the services to the host, open the url in the port provided by the command. Example http://127.0.0.1:55453

```bash
minikube service k8app-backend --url
```

#### k8s folder

1) Enable minikube to see local Docker images: ```eval $(minikube -p minikube docker-env)```
2) Rebuild the docker images so now minikube sees them ```docker-compose build```
3) To enable the NGINX Ingress controller, run the following command: ```minikube addons enable ingress```.
3) Install metrics server for
   minikube ```kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml```
   so minikube can measure utilization of deployment (needed for HPA)
3) Navigate to ```k8s``` folder and run ```kubectl delete -f .;kubectl apply -f .```
4) Create a tunnel to load balancer with minikube: ```minikube service lb-backend``` or ```minikube tunnel lb-backend```
5) Follow generate tunnel URI with to see backend container

#### Google Cloud

`k8s-gcp` contains YAML (maybe HELM) files for GCP.

To set up dependencies - consult
this [guide](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl)

```bash
# Connect kubectl to google cloud
gcloud container clusters get-credentials autopilot-cluster-1 --region us-central1
```

## Tech stack

### Backend

Backend is built using Python and FastAPI framework.

### Frontend

Backend is built on React component and is run using npm.

### Database

Postgres is used as primary data store. Credentials can be found in .env file.

## Further details

See detailed docs on ```backend``` and ```frontend``` in corresponding folders.

TODO

- Seems like when you delete something from the frontend it still exists in the database 
