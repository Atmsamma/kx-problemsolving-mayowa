# Mayowa Ajijola Flask app instructions


## Prerequisites

Install docker
Install docker compose
Install git bash


## Starting the application
* Clone this repo using git clone https://github.com/zvenczel-kx/kx-problemsolving-mayowa.git
* Open your preferred terminal and cd into the kx-problemsolving-mayowa directory
* Run docker compose up or docker-compose up
* Wait for application to build and run


## Starting the application
* Open you preferred browser and type http://localhost/5000 in the search
If running properly it should return {"message":"Welcome to the Dockerized Flask MongoDB app!","status":true}
* To check the status of the containers use the http://localhost:5000/status endpoint
* To receive data from the database use http://localhost:5000/data endpoint
