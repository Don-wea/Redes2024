#!/bin/bash

# Variables
NETWORK_NAME="redes2024_network"
CONTAINER_NAME="redes2024_container_server"
IMAGE_NAME="my-wifi-server:latest"  
POSTGRES_USER="admin"
POSTGRES_PASSWORD="Redes2024"
PORT="5432"
VOLUME_NAME="redes2024_volume"

SOCKETPORT="44555"

# Check if the network exists
if docker network ls --filter "name=^${NETWORK_NAME}$" --format "{{.Name}}" | grep -w "${NETWORK_NAME}" > /dev/null; then
    echo "Network ${NETWORK_NAME} already exists."
else
    echo "Creating network: ${NETWORK_NAME}"
    docker network create "${NETWORK_NAME}"
fi

# Check if the volume exists
if docker volume ls --filter "name=^${VOLUME_NAME}$" --format "{{.Name}}" | grep -w "${VOLUME_NAME}" > /dev/null; then
    echo "Volume ${VOLUME_NAME} already exists."
else
    echo "Creating volume: ${VOLUME_NAME}"
    docker volume create "${VOLUME_NAME}"
fi

# Check if the container already exists
if docker ps -a --filter "name=^${CONTAINER_NAME}$" --format "{{.Names}}" | grep -w "${CONTAINER_NAME}" > /dev/null; then
    echo "Container ${CONTAINER_NAME} already exists. Removing it..."
    docker rm -f "${CONTAINER_NAME}"
fi

echo "Starting container: $CONTAINER_NAME"
docker run --rm \
    --network "${NETWORK_NAME}" \
    --name "${CONTAINER_NAME}" \
    -e POSTGRES_USER="${POSTGRES_USER}" \
    -e POSTGRES_PASSWORD="${POSTGRES_PASSWORD}" \
    -p "${PORT}:${PORT}" \
    -v "${VOLUME_NAME}:/var/lib/postgresql/data" \
    "${IMAGE_NAME}" \
    __innit__/innitRun.sh --host "$CONTAINER_NAME" --port "$SOCKETPORT"

# # --- Clean up ---
# echo "Cleaning up network: $NETWORK_NAME"
# docker network rm "$NETWORK_NAME"

# echo "Cleaning up unused volumes"
# docker volume prune -f

# echo "Cleaning up unused containers"
# docker container prune -f
