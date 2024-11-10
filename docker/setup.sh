#!/bin/bash

sudo ./docker/build1environment.sh
sudo ./docker/build2dependencies.sh
sudo ./docker/build3code.sh
sudo ./docker/build4runtime.sh