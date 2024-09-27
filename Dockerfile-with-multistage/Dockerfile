# Build stage
FROM python:3.10-slim AS builder

WORKDIR /app
COPY backend/requirements.txt ./
RUN pip install --user -r requirements.txt

# Production stage
FROM python:3.10-slim

WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY backend/ .

ENV PATH=/root/.local/bin:$PATH

# Expose the port the service runs on
EXPOSE 8080

# Command to run the app
CMD ["python", "app.py"]

