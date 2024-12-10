#!/bin/bash

echo - --- Images --- -
docker images
echo

echo - --- Containers --- -
docker container ls
echo

# echo - --- running containers --- -
# docker ps 
# echo

echo - --- Volumes --- -
docker volume ls
echo

echo - --- Networks --- -
docker network ls
echo

