#!/bin/bash

CONTAINER_NAME="redes2024_container_server"
SOCKETPORT="44555"

# Start PostgreSQL service
service postgresql start

# give permission to scripts
chmod +x ./*.sh
chmod +x ./__innit__/*.sh

# modify PostgreSql configuration
./__innit__/postgreSqlInnit.sh

# Run the Python server
python3 src/server.py --host "$CONTAINER_NAME" --port "$SOCKETPORT"