#!/bin/bash

# Start the server in a new terminal window
gnome-terminal -- bash -c "python server/server.py; exec bash"

# Start the client in a new terminal window
gnome-terminal -- bash -c "python client/client.py; exec bash"
