#!/bin/bash

# delete all stopped containers
docker container prune -f

# clean up everything unused
docker system prune -a --volumes -f

# prune unused images
docker image prune -a -f



