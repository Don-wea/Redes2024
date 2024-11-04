# Base image for Raspberry Pi (use the correct version for your device)
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY src /app

# Install required Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the server
EXPOSE 5000

# Run the server
CMD ["python", "server.py"]
