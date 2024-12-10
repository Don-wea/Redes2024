#!/bin/bash

# Variables
NETWORK_NAME="redes2024_network"
CONTAINER_NAME="redes2024_container_server"
IMAGE_NAME="my-wifi-server:latest"
PS_USER="admin"
PS_PASSWORD="Redes2024"
DATABASE="mainDB"
LOCALHOST="30432"
PORT="5432"
VOLUME_NAME="redes2024_volume"


# Run the container
echo "Starting container: ${CONTAINER_NAME}"
docker exec -it \
    --user "${POSTGRES_USER}" \
    /bin/bash

    # docker run -it \
    # --name postgres-container \
    # -e TZ=UTC \
    # -p 30432:5432 \
    # -e POSTGRES_PASSWORD=My:s3Cr3t/ \
    # "${IMAGE_NAME}" \
    # /bin/bash

