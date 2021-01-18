# RESTful-Kubernetes-project

Small shopping list REST API project that can be deployed to a local Kubernetes cluster.
(Deployment to the Kubernetes cluster is still a work in progress)

To get the project, clone it with Git:

    git clone git@github.com:AndersBennedsgaard/RESTful-Kubernetes-project.git
    cd RESTful-Kubernetes-project/

## Automated deployment to a Kubernetes cluster (WIP)
Have Docker and kubectl installed, with a Kubernetes cluster running:

    ./deploy

The API should be accessible through http://localhost:8000 now.

## Manual deployment
Create a Docker image:

    docker build -f Docker/Dockerfile -t shopping-list:latest .

Optionally, the API can be accessed by running the Docker container (use -d to daemonize it):

    docker run -p 8000:5000 shopping-list

The API should be accessible through http://localhost:8000 now.

It can now be deployed to a Kubernetes Cluster, by running:

    kubectl apply -f Kubernetes/flask-service.yml
    kubectl apply -f Kubernetes/flask-deployment.yml

Again, the API should be accessible through http://localhost:8000 now if run on a local cluster.

## Development installation 
Have Python and pip installed:
    
    virtualenv .
    (Linux/Mac): source bin/activate
    (Windows): Scripts/activate.bat
    pip install -r requirements.txt

## Run API in development mode
Run a development server in the terminal, which can be accessed through http://localhost:5000:

    (Linux/Mac): ./run_server
    (Windows): run_server.bat

With requests (a Python package) the API can be interacted with, at 
> http://localhost:5000/

A Python example script can be found in `example_script.py`. 
When the server is running, the script can be run by simply calling 

    python example_script.py

If cURL is more to your liking, this does the same as the Python script:

    BASE_URL="http://localhost:5000"

    echo "GET all"
    RES=$(curl --write-out '%{http_code}' --silent $BASE_URL/shoppinglist)
    N_ENTRIES=$(echo "$RES" | grep "name" -o | wc -l)
    echo "Number of entries: $N_ENTRIES"

    echo "POST item"
    curl --silent -X POST "$BASE_URL"/shoppinglist -d 'name=keyboard&quantity=2'
    NEW_ENTRY_ID=$((N_ENTRIES+1))

    echo "GET item with id $NEW_ENTRY_ID"
    curl --silent "$BASE_URL"/shoppinglist/"$NEW_ENTRY_ID"

    echo "PUT item with id $NEW_ENTRY_ID with new resources"
    curl --silent -X PUT "$BASE_URL"/shoppinglist/"$NEW_ENTRY_ID" -d 'quantity=4&note=The cheap one'

    echo "DELETE item with id $NEW_ENTRY_ID"
    curl --silent -X DELETE "$BASE_URL"/shoppinglist/"$NEW_ENTRY_ID"

    echo "GET item with id $NEW_ENTRY_ID"
    curl --silent "$BASE_URL"/shoppinglist/"$NEW_ENTRY_ID"

## Run tests

    pytest -v
