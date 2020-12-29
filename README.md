# RESTful-Kubernetes-project

Small REST API project that can be deployed to a Kubernetes cluster.

(Docker and Kubernetes not set up as of yet)

## Installation (not tested): 
Have Python, pip, and Git installed:
    
    git clone git@github.com:AndersBennedsgaard/RESTful-Kubernetes-project.git
    cd RESTful-Kubernetes-project/
    virtualvenv .
    pip install -r requirements.txt

## Run API
Run a development server in the terminal, which can be accessed through http://localhost:5000
    
    cd RESTful-Kubernetes-project
    python wsgi.py

With requests (a Python package) the API can be interacted with, at 
> http://localhost:5000/shoppinglist

and

> http://localhost:5000/shoppinglist/item_id

where item_id is an integer.

## Run tests

    cd RESTful-Kubernetes-project
    pytest -v
