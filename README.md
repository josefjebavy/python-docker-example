# python-docker-example
Python example of using Docker

python api documentation:
https://docker-py.readthedocs.io/en/stable/#

# README #

### manual build ###
docker build -t python-docker-app .

### manual run with mount local source ###

docker run -it --rm -v $PWD:/usr/src/app -v /var/run/docker.sock:/var/run/docker.sock --name python-docker-app-run python-docker-app /bin/bash 

### run ###
docker-compose up
