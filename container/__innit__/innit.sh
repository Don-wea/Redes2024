#!/bin/bash

# Start PostgreSQL service
service postgresql start

# give permission to scripts
chmod +x ./*.sh
chmod +x ./__innit__/*.sh

# modify PostgreSql configuration
./__innit__/postgreSqlInnit.sh
