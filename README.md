# RESTful-Kubernetes-project

Small shopping list REST API project that can be deployed to a Kubernetes cluster.
(K8s continuously in a CrashLoopBackOff as of now..)

## Installation: 
Have Python, pip, and Git installed:
    
    git clone git@github.com:AndersBennedsgaard/RESTful-Kubernetes-project.git
    cd RESTful-Kubernetes-project/
    virtualenv .
    (Linux/Mac): source bin/activate
    (Windows): Scripts/activate.bat
    pip install -r requirements.txt

## Run API
Run a development server in the terminal, which can be accessed through http://localhost:5000:

    cd RESTful-Kubernetes-project
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

    cd RESTful-Kubernetes-project
    pytest -v
