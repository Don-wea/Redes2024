#!/bin/bash

# muestra por consola todas las imagenes, contenedores, volumenes y networks existentes.

echo - --- Images --- -
docker images
echo

echo - --- Containers --- -
docker container ls
echo

echo - --- Volumes --- -
docker volume ls
echo

echo - --- Networks --- -
docker network ls
echo

