# Single Stage Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY backend/ .

# Expose the port the service runs on
EXPOSE 8080

# Command to run the app
CMD ["python", "app.py"]

