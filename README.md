Python Task Scheduling Setup
<br>
This guide outlines the steps to set up a backend for Python Task Scheduling.
<br>

Backend Setup
<br>

1. Installation
   <br>
   Install the required dependencies for the backend:
   <br>

pip install -r requirements.txt
<br> 2. Start the Backend Server
<br>
Using Docker
<br>
Run the following command to build and start your Docker containers:
<br>

docker-compose up --build
<br>
Without Docker
<br>
If you prefer to run the services manually, follow these steps:
<br>

Start RabbitMQ:
<br>

rabbitmq-server
<br>
Start Celery:
<br>

celery -A your_project_name worker --loglevel=info
<br>
Run your Python application:
<br>

Technologies Used
<br>
Backend: Python, Celery, RabbitMQ
<br>
Containerization: Docker
<br>
