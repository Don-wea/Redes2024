#!/bin/bash

# Variables
NETWORK_NAME="redes2024_network"
CLIENT_CONTAINER="redes2024_container_client"
IMAGE_NAME="my-wifi-client:latest"  

# Step 1: Check if the network exists, and create it if it doesn’t
if ! docker network ls --filter name=^${NETWORK_NAME}$ --format "{{.Name}}" | grep -w "$NETWORK_NAME" > /dev/null; then
    echo "Creating network: $NETWORK_NAME"
    docker network create "$NETWORK_NAME"
else
    echo "Network $NETWORK_NAME already exists."
fi

# Step 2: Check if the container already exists, and remove it if it does
if docker ps -a --filter name=^/${CLIENT_CONTAINER}$ --format "{{.Names}}" | grep -w "$CLIENT_CONTAINER" > /dev/null; then
    echo "Container $CLIENT_CONTAINER already exists. Removing it..."
    docker rm -f "$CLIENT_CONTAINER"
fi

# Step 3: Start the container with an interactive shell
echo "Starting container: $CLIENT_CONTAINER in interactive mode"
docker run --rm -it \
    --network "$NETWORK_NAME" \
    --name "$CLIENT_CONTAINER" \
    "$IMAGE_NAME" \
    /bin/bash
