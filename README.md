# Python Task Scheduling Setup

This guide outlines the steps to set up a backend Python Task Scheduling using Celery, RabbitMQ, and Docker.

## Backend Setup

### 1. Installation

Install the required dependencies for the backend:

```bash
pip install -r requirements.txt
2. Start the Backend Server
Using Docker
Run the following command to build and start your Docker containers:

bash
Copy code
docker-compose up --build
Without Docker
If you prefer to run the services manually, follow these steps:

Start RabbitMQ:

bash
Copy code
rabbitmq-server
Start Celery:

bash
Copy code
celery -A your_project_name worker --loglevel=info
Run your Python application:

bash
Copy code
python app.py
Technologies Used
Backend: Python, Celery, RabbitMQ
Containerization: Docker
```
