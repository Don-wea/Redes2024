#!/bin/bash

# Define your image and tag
DOCKERFILE_NAME="Dockerfile.1environment"
IMAGE_NAME="my-wifi-client"

# current stage
TAG1="environment-latest"
#stage 2
TAG2="dependencies-latest"
#stage 3
TAG3="code-latest"
#stage 4
TAG4="runtime-latest"

# List of tags in reverse order (from most recent to earliest)
TAGS=("$TAG4" "$TAG3" "$TAG2" "$TAG1")

# Loop through each tag, check if it exists, and remove the image if it does
for TAG in "${TAGS[@]}"; do
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
done


# Build the new image
echo "Building new image: $IMAGE_NAME:$TAG1"
docker build -f ./client/docker/dockerfiles/$DOCKERFILE_NAME -t "$IMAGE_NAME:$TAG1" .
