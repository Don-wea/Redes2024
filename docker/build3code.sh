#!/bin/bash

# Define your image and tag
BASE_IMAGE_NAME="my-wifi-server:dependencies-latest"
DOCKERFILE_NAME="Dockerfile.3code"
IMAGE_NAME="my-wifi-server"

# current stage
TAG3="code-latest"
#stage 4
TAG4="runtime-latest"

# List of tags in reverse order (from most recent to earliest)
TAGS=("$TAG4" "$TAG3")

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


# Build the new image with the base image argument
echo "Building new image: $IMAGE_NAME:$TAG3"
docker build -f ./docker/dockerfiles/$DOCKERFILE_NAME -t "$IMAGE_NAME:$TAG3" --build-arg BASE_IMAGE="$BASE_IMAGE_NAME" .