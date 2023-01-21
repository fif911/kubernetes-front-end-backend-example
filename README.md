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

#### k8s folder

1) Enable minikube to see local Docker images: ```eval $(minikube -p minikube docker-env) ```
2) Rebuild the docker images so now minikube sees them ```docker-compose up --build; docker-compose down```
3) Navigate to ```k8s``` folder and run ```kubectl apply -f .```
4) Create a tunnel to load balancer with minikube: ```minikube service lb-backend``` or ```minikube tunnel lb-backend```
5) Follow generate tunnel URI with to see backend container

## Tech stack

### Backend

Backend is built using Python and FastAPI framework.

### Frontend

Backend is built on React component and is run using npm.

### Database

Postgres is used as primary data store. Credentials can be found in .env file.

## Further details

See detailed docs on ```backend``` and ```frontend``` in corresponding folders.