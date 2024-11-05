#!/bin/bash

# always use 'sudo'


# check all images
docker images

# remove an image
docker rmi <image_id_or_name:tag>

# remove all images
docker  rmi -f $(docker images -q)

# prune unused images
docker system prune -af

# clean up everything unused
docker system prune -a --volumes
