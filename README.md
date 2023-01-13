# Simple containerized application

This is a **TodoList application** which has **backend, frontend and database**.

## How to run:

1) Go inside k8app folder
2) Run ```docker-compose up```
3) Navigate to **frontend** http://localhost:1337/
3) Navigate to **backend** http://localhost:8080/
4) Check out main page and visit http://localhost:8080/docs to play with API
5) If you wish you can connect to PostgresDB (find credentials in .env file) to investigate the items table and data
   stored in it

## Tech stack

### Backend

Backend is built using Python and FastAPI framework.

### Frontend

Backend is built on React component and is run using npm.

### Database

Postgres is used as primary data store. Credentials can be found in .env file.

## Further details

See detailed docs on ```backend``` and ```frontend``` in corresponding folders.