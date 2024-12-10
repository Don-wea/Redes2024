#!/bin/bash

# Variables
CONTAINER_NAME="redes2024_container_server"
SQL_SCRIPT_PATH="./database/mainDB.sql" # Adjust to the path of your .sql file in the container
DB_USER="postgres"

echo "Executing SQL script inside container: ${CONTAINER_NAME}"

# Execute SQL script inside the container
docker exec -u "${DB_USER}" -i "${CONTAINER_NAME}" psql -U "${DB_USER}" -d "${DATABASE}" -f "${SQL_SCRIPT_PATH}"

if [ $? -eq 0 ]; then
    echo "Database initialized successfully."
else
    echo "Failed to execute SQL script."
    exit 1
fi
