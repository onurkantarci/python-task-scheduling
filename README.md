# Python Task Scheduling Setup

<br>
This guide outlines the steps to set up a backend Python Task Scheduling using Celery, RabbitMQ, and Docker.
<br>

## Backend Setup

<br>

### 1. Installation

<br>
Install the required dependencies for the backend:
<br>

```bash
pip install -r requirements.txt
<br>
2. Start the Backend Server
<br>
Using Docker
<br>
Run the following command to build and start your Docker containers:
<br>
bash
Copy code
docker-compose up --build
<br>
Without Docker
<br>
If you prefer to run the services manually, follow these steps:
<br>
Start RabbitMQ:
<br>

bash
Copy code
rabbitmq-server
<br>
Start Celery:
<br>

bash
Copy code
celery -A your_project_name worker --loglevel=info
<br>
Run your Python application:
<br>

bash
Copy code
python app.py
<br>
Technologies Used
<br>
- **Backend**: Python, Celery, RabbitMQ
- **Containerization**: Docker
```
