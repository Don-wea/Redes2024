#!/bin/bash

# este archivo inicializa el container en segundo plano. despues del 'setup.sh' se ejecuta este archivo para crear que el container este en funcionamiento.

# setup.sh -> start.sh -> startDB.sh -> run.sh


# Variables
NETWORK_NAME="redes2024_network"
CONTAINER_NAME="redes2024_container_server"
IMAGE_NAME="my-wifi-server:latest"
#PS_USER="postgres"
PS_PASSWORD="Redes2024"
DATABASE="mainDB"
LOCALHOST="30432"
PORT="5432"
VOLUME_NAME="redes2024_volume"

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

# Run the container
echo "Starting container: ${CONTAINER_NAME}"
docker run -d\
    --network "${NETWORK_NAME}" \
    --name "${CONTAINER_NAME}" \
    -e TZ=UTC \
    -e POSTGRES_PASSWORD="${PS_PASSWORD}" \
    -e POSTGRES_DB="${DATABASE}" \
    -p "${LOCALHOST}:${PORT}" \
    -v "${VOLUME_NAME}:/var/lib/postgresql/data" \
    "${IMAGE_NAME}"

    # docker run -it \
    # --name postgres-container \
    # -e TZ=UTC \
    # -p 30432:5432 \
    # -e POSTGRES_PASSWORD=My:s3Cr3t/ \
    # "${IMAGE_NAME}" \
    # /bin/bash

