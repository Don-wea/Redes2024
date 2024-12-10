#!/bin/bash

echo "--- running server ---"

CONTAINER_NAME="redes2024_container_server"
SOCKETPORT="44555"

python3 "src/server.py" --host $CONTAINER_NAME --port $SOCKETPORT