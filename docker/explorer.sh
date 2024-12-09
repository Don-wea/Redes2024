#!/bin/bash

# Variables
NETWORK_NAME="redes2024_network"
CONTAINER_NAME="redes2024_container_server"
IMAGE_NAME="my-wifi-server:latest"  
POSTGRES_PASSWORD="Redes2024"
PORT="5432"

# Step 1: Create a Docker network
if docker network ls --filter name=^${NETWORK_NAME}$ --format "{{.Name}}" | grep -w "$NETWORK_NAME" > /dev/null; then
    echo "Network $NETWORK_NAME already exists. Removing it..."
    docker network rm "$NETWORK_NAME"
fi

echo "Creating network: $NETWORK_NAME"
docker network create "$NETWORK_NAME"


# Step 2: Run the container on the created network and execute main.py
if docker ps -a --filter name=^/${CONTAINER_NAME}$ --format "{{.Names}}" | grep -w "$CONTAINER_NAME" > /dev/null; then
    echo "Container $CONTAINER_NAME already exists. Removing it..."
    docker rm -f "$CONTAINER_NAME"
fi

echo "Starting container: $CONTAINER_NAME in interactive mode"
docker run --rm -it \
    --network "$NETWORK_NAME" \
    --name "$CONTAINER_NAME" \
    -e POSTGRES_PASSWORD="$POSTGRES_PASSWORD" \
    -p "$PORT:$PORT" \
    "$IMAGE_NAME" \
    /bin/bash


# --- Clean up ---
echo "Cleaning up network: $NETWORK_NAME"
docker network rm "$NETWORK_NAME"

echo "Cleaning up unused volumes"
docker volume prune -f

echo "Cleaning up unused containers"
docker container prune -f