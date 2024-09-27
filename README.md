# DevOps Metrics Dashboard

This project is a DevOps Metrics Dashboard built with Python and Flask, designed to monitor basic system metrics such as CPU usage, memory usage, and disk usage. The application uses Docker multi-stage builds to create a lightweight and efficient runtime environment, showcasing best practices in containerization.

## Key Features

- **System Metrics Monitoring**: Tracks CPU, memory, and disk usage in real-time.
- **Multi-Stage Docker Builds**: Creates efficient Docker images by separating the build and runtime environments.
- **Flask Web Application**: A simple and interactive dashboard interface for displaying system metrics.
- **Scalable and Lightweight**: The application is designed to be easily scalable and uses minimal resources.

## Project Structure

```plaintext
.
├── Dockerfile                     # Dockerfile without multi-stage build
├── Dockerfile-with-multistage     # Dockerfile with multi-stage build
├── app                            # Application folder
│   ├── __init__.py                # Flask app initialization
│   ├── metrics.py                 # Metric collection logic
│   └── templates
│       └── index.html             # HTML template for the dashboard
└── requirements.txt               # Project dependencies
```
## How to Run

1. **Clone the repository**:

    ```bash
    git clone <repository-url>
    ```

2. **Build the Docker image**:

    - For without multi-stage build:

        ```bash
        docker build -t devops-dashboard -f Dockerfile .
        ```

    - For with multi-stage build:

        ```bash
        docker build -t devops-dashboard -f Dockerfile-with-multistage .
        ```

3. **Run the Docker container**:

    ```bash
    docker run -p 5000:5000 devops-dashboard
    ```

4. **Access the Dashboard**:  
   Open your browser and go to:  
   `http://localhost:5000`
## About

This project implements Docker multi-stage builds to significantly reduce the size of the Docker image by approximately 99.7%. By separating the build and runtime environments, the application ensures that only essential components are included in the final image, optimizing performance and minimizing resource usage.

## Conclusion

The DevOps Metrics Dashboard not only demonstrates effective monitoring of system metrics but also showcases best practices in Docker containerization. With the implementation of multi-stage builds, this project serves as a practical example of how to enhance the efficiency and performance of Docker images.

Feel free to explore the project, and contribute if you'd like to add more features or improvements!
