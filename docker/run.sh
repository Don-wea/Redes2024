#!/bin/bash

# ejecuta el servidor principal del programa.

# setup.sh -> start.sh -> startDB.sh -> run.sh

# Variables
CONTAINER_NAME="redes2024_container_server"
PYTHON_SCRIPT_PATH="./src/server.py" # Adjust to the path of your Python script in the container

echo "Running Python program inside container: ${CONTAINER_NAME}"

# Run the Python program
docker exec -it "${CONTAINER_NAME}" python3 "${PYTHON_SCRIPT_PATH}"

if [ $? -eq 0 ]; then
    echo "Python program executed successfully."
else
    echo "Failed to run Python program."
    exit 1
fi
