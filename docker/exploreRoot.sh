#!/bin/bash

# Explorar el container con acceso 'root'



# Variables
CONTAINER_NAME="redes2024_container_server" 
POSTGRES_USER="root"


docker exec -it --user "${POSTGRES_USER}" "${CONTAINER_NAME}" /bin/bash
