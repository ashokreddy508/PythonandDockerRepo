## Git clone the application
## Used Python3.X
## Create a virtual environment inside the application

```python

    virtualenv -p /usr/bin/python3 venv    

    source venv/bin/activate

```

## Install Python modules

```python

   pip3 install -r requirements.txt

```


## Run the application using

```python

    python3 app.py

```


## You will get below REST API

```python

        http://localhost:8080/info

```


## Docker commands

```bash

        // List all running container
        docker ps

        // list all containers
        docker ps -a

        // list all docker images
        docker images

        // build a docker image
        docker build -t <imageName:version> dockerFilePath
        docker build -t flaskapp:latest .


        // run a docker container in daemon mode with ports exposed
        docker run -d -p <outsidePort>:<dockerInsidePort> <imageName:version>
        docker run -d -p 8080:8080 flaskapp

        // List all running container
        docker ps

        // Verify the Application using the below URL
        http://localhost:8080/info

```
