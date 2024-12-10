#!/bin/bash

# ./docker/build1environment.sh
# ./docker/build2dependencies.sh
# ./docker/build3code.sh
# ./docker/build4runtime.sh

#!/bin/bash

# Pull image only if it doesn't exist
if ! docker images -q "ubuntu/postgres:latest"; then
    echo "Image not found, pulling: ubuntu/postgres:latest"
    docker pull ubuntu/postgres:latest
else 
    echo "Image already exists: ubuntu/postgres:latest"
fi

# Define your image and tag
BASE_IMAGE_NAME="ubuntu/postgres:latest"
DOCKERFILE_NAME="Dockerfile.main"
IMAGE_NAME="my-wifi-server"

# current stage
TAG="latest"


# # Loop through each tag, check if it exists, and remove the image if it does

# if docker images -q "$IMAGE_NAME:$TAG"; then
#     echo "Removing old image: $IMAGE_NAME:$TAG"

#     # Stop and remove all containers using the image
#     containers=$(docker ps -a -q --filter ancestor="$IMAGE_NAME:$TAG")
#     if [ -n "$containers" ]; then
#         echo "Stopping and removing containers using $IMAGE_NAME:$TAG"
#         docker rm -f $containers
#     fi

#     # Remove the image
#     docker rmi "$IMAGE_NAME:$TAG" -f
# fi


# Build the new image
echo "Building new image: $IMAGE_NAME:$TAG"
docker build -f ./docker/dockerfiles/$DOCKERFILE_NAME -t "$IMAGE_NAME:$TAG" --build-arg BASE_IMAGE="$BASE_IMAGE_NAME" .