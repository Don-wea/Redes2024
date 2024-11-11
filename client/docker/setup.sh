#!/bin/bash

./client/docker/build1environment.sh
./client/docker/build2dependencies.sh
./client/docker/build3code.sh
./client/docker/build4runtime.sh