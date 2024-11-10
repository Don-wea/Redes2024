#!/bin/bash

sudo ./client/docker/build1environment.sh
sudo ./client/docker/build2dependencies.sh
sudo ./client/docker/build3code.sh
sudo ./client/docker/build4runtime.sh