#!/bin/bash

# Abre el archivo log, aquel que se encuentra dentro del container.

# Variables
CONTAINER_NAME="redes2024_container_server"
LOG_PATH="./eventos.log" # Adjust to the path of your Python script in the container

echo "Executing log file in the container: ${CONTAINER_NAME}"

# Open the log
docker exec -it "${CONTAINER_NAME}" nano "${LOG_PATH}"

if [ $? -eq 0 ]; then
    echo "Log file opened"
else
    echo "Failed to open log file."
    exit 1
fi