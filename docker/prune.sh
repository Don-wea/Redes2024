#!/bin/bash


# prune unused images
docker image prune -a -f

# clean up everything unused
docker system prune -a --volumes -f

# delete all stopped containers
docker container prune -f