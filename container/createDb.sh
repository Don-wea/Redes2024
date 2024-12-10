#!/bin/bash

# Variables
SQL_SCRIPT_PATH="./database/mainDB.sql"     # Path to your .sql script inside the container
DB_USER="root"                          # PostgreSQL user
DB_NAME="mainDB"                            # Initial database (can change if needed)
DB_PASSWORD="Redes2024"                     # PostgreSQL password for the user

# Check if the SQL script exists
if [ ! -f "$SQL_SCRIPT_PATH" ]; then
    echo "SQL script $SQL_SCRIPT_PATH not found!"
    exit 1
fi

# Set PGPASSWORD environment variable
export PGPASSWORD="$DB_PASSWORD"

# Execute the SQL script
echo "Executing SQL script: $SQL_SCRIPT_PATH"
psql -U "$DB_USER" -d "$DB_NAME" -f "$SQL_SCRIPT_PATH" -w

echo "Database setup complete."
