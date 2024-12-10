#!/bin/bash

# elimina todos los datos no utilizados de docker 
# peligro: podria pasar a eliminar la imagen base del proyecto, si no tienes buena conexion a internet, ten cuidado de borrar la imagen principal.

# delete all stopped containers
docker container prune -f

# clean up everything unused
docker system prune -a --volumes -f

# prune unused images
docker image prune -a -f



