#!/bin/bash

echo --- images ---
docker images
echo

echo --- containers ---
docker container ls
echo

# echo --- running containers ---
# docker ps 
# echo

echo --- volumes ---
docker volume ls

echo --- networks ---
docker network ls
echo

