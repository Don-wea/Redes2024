#!/bin/bash

# Variables
SQL_SCRIPT_PATH="./database/mainDB.sql"     # Path to your .sql script inside the container
DB_USER="postgres"                         # PostgreSQL user
DB_PASSWORD="Redes2024"                    # PostgreSQL password for the user
DB_NAME="mainDB"                           # Database name

# Create system user for PostgreSQL
useradd -m $DB_USER


# Set the PostgreSQL password for authentication
export PGPASSWORD="$DB_PASSWORD"

# Create the database if it doesn't exist
echo "Creating database ${DB_NAME}..."
createdb --username="$DB_USER" "$DB_NAME" -w


# Grant all privileges to the user
echo "Granting all privileges on database ${DB_NAME} to ${DB_USER}..."
psql -U postgres -d "$DB_NAME" -c "GRANT ALL PRIVILEGES ON DATABASE ${DB_NAME} TO ${DB_USER};"


# Check if the SQL script exists
if [ ! -f "$SQL_SCRIPT_PATH" ]; then
    echo "SQL script $SQL_SCRIPT_PATH not found!"
    exit 1
fi

# Execute the SQL script
echo "Executing SQL script: $SQL_SCRIPT_PATH"
psql -U "$DB_USER" -d "$DB_NAME" -f "$SQL_SCRIPT_PATH" -w


echo "Database setup complete."
