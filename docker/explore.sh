#!/bin/bash

# Explorar el container con acceso 'postgres', para manejar base de datos


# Variables
CONTAINER_NAME="redes2024_container_server" 
POSTGRES_USER="postgres"


docker exec -it --user "${POSTGRES_USER}" "${CONTAINER_NAME}" /bin/bash
