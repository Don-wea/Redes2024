#!/bin/bash

# Variables
NETWORK_NAME="redes2024_network"
SERVER_CONTAINER="redes2024_container_server"
CLIENT_CONTAINER="redes2024_container_client"
IMAGE_NAME="my-wifi-client:latest"  
PORT="5432"
SOCKETPORT="44555"



# Run the container on the created network and execute main.py

if docker ps -a --filter name=^/${CLIENT_CONTAINER}$ --format "{{.Names}}" | grep -w "$CLIENT_CONTAINER" > /dev/null; then
    echo "Container $CLIENT_CONTAINER already exists. Removing it..."
    docker rm -f "$CLIENT_CONTAINER"
fi

echo "Starting container: $CLIENT_CONTAINER"

docker run --rm \
    --network "$NETWORK_NAME" \
    --name "$CLIENT_CONTAINER" \
    "$IMAGE_NAME" \
    python3 src/client.py --host "$SERVER_CONTAINER" --port "$SOCKETPORT"
