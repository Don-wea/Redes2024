#!/bin/bash

# Define your image and tag
DOCKERFILE_NAME="Dockerfile.main"
IMAGE_NAME="my-wifi-client"
TAG="latest"


# Loop through each tag, check if it exists, and remove the image if it does

if docker images -q "$IMAGE_NAME:$TAG"; then
    echo "Removing old image: $IMAGE_NAME:$TAG"

    # Stop and remove all containers using the image
    containers=$(docker ps -a -q --filter ancestor="$IMAGE_NAME:$TAG")
    if [ -n "$containers" ]; then
        echo "Stopping and removing containers using $IMAGE_NAME:$TAG"
        docker rm -f $containers
    fi

    # Remove the image
    docker rmi "$IMAGE_NAME:$TAG" -f
fi


# Build the new image
echo "Building new image: $IMAGE_NAME:$TAG"
docker build -f ./client/docker/dockerfiles/$DOCKERFILE_NAME -t "$IMAGE_NAME:$TAG" .
