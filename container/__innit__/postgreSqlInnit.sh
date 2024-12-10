#!/bin/bash

# # Set the PostgreSQL password for the postgres user
# DB_PASSWORD="Redes2024"

# # Find the location of the pg_hba.conf file
# PG_HBA_FILE=$(find / -name "pg_hba.conf" 2>/dev/null | head -n 1)

# # Check if pg_hba.conf file is found
# if [ -z "$PG_HBA_FILE" ]; then
#   echo "pg_hba.conf file not found!"
#   exit 1
# fi

# # Display current pg_hba.conf content (before modification)
# echo "Current pg_hba.conf content:"
# cat "$PG_HBA_FILE"
# echo

# # Backup pg_hba.conf before modifying
# cp "$PG_HBA_FILE" "$PG_HBA_FILE.bak"
# echo "Backup of pg_hba.conf created as $PG_HBA_FILE.bak"

# # Modify the authentication method for postgres user to 'md5' (password authentication)
# echo "Modifying authentication method for postgres user to md5..."
# sed -i 's/peer/md5/' "$PG_HBA_FILE"

# # Set the password for the postgres user
# echo "Setting password for postgres user..."
# psql -U postgres -c "ALTER USER postgres PASSWORD '$DB_PASSWORD';"

# # Display the updated pg_hba.conf content
# echo "Updated pg_hba.conf content:"
# cat "$PG_HBA_FILE"
# echo

# # Restart PostgreSQL service to apply changes
# echo "Restarting PostgreSQL service..."
# service postgresql restart

# echo "PostgreSQL authentication and password setup complete. PostgreSQL has been restarted."
