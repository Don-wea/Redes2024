#!/bin/bash

# Define your image and tag
BASE_IMAGE_NAME="my-wifi-server:code-latest"
DOCKERFILE_NAME="Dockerfile.4runtime"
IMAGE_NAME="my-wifi-server"

# current stage
TAG4="runtime-latest"

# List of tags in reverse order (from most recent to earliest)
TAGS=("$TAG4")

# Loop through each tag, check if it exists and remove the image if it does
for TAG in "${TAGS[@]}"; do
    if sudo docker images -q "$IMAGE_NAME:$TAG"; then
        echo "Removing old image: $IMAGE_NAME:$TAG"
        sudo docker rmi "$IMAGE_NAME:$TAG" -f
    fi
done

# Build the new image with the base image argument
echo "Building new image: $IMAGE_NAME:$TAG4"
docker build -f ./docker/dockerfiles/$DOCKERFILE_NAME -t "$IMAGE_NAME:$TAG4" --build-arg BASE_IMAGE="$BASE_IMAGE_NAME" .