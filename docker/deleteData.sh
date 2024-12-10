#!/bin/bash

# elimina el container y su respectivo volumen con informacion, eliminar el volumen significa reiniciar la base de datos y toda la informacion almacenada.

# remove container
docker container rm redes2024_container_server -f

# remove volume
docker volume rm redes2024_volume -f
