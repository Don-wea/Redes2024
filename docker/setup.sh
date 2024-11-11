#!/bin/bash

./docker/build1environment.sh
./docker/build2dependencies.sh
./docker/build3code.sh
./docker/build4runtime.sh