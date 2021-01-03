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
Run a development server in the terminal, which can be accessed through http://localhost:5000:
    
    cd RESTful-Kubernetes-project
    ./run_server

With requests (a Python package) the API can be interacted with, at 
> http://localhost:5000/

An example script can also be found in `example_script.py`. 
When the server is running, the script can be run by simply calling 

    python example_script.py

## Run tests

    cd RESTful-Kubernetes-project
    pytest -v
