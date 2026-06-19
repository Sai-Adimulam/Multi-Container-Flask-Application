# Multi-Container-Flask-Application

# Multi-Container Flask Application using Docker Compose

## Project Overview

This project demonstrates how to:

* Build a single Docker image
* Create multiple containers from the same image
* Use Docker Volumes for persistent storage
* Use Docker Networks for container communication
* Manage containers using Docker Compose

---

## Project Architecture

```text
                Docker Network
                       |
        --------------------------------
        |                              |
   Container-A                   Container-B
      Port 4000                    Port 4001
        |                              |
        --------------------------------
                       |
                  Docker Image
                    image-1
                       |
                  Docker Volume
                    volume-a
```

---

## Technologies Used

* Python
* Flask
* Docker
* Docker Compose

---

## Project Structure

```text
Multi-Container-Flask-Application/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## Flask Application Routes

### Home Page

```text
/
```

Response:

```text
Welcome to Docker Project
```

### Health Check

```text
/health
```

Response:

```text
Application is Healthy
```

### Version

```text
/version
```

Response:

```text
Version 2.0
```

### Info

```text
/info
```

Response:

```text
Container Project Version 2.0 | Running inside Docker
```

---

## Docker Image

Image Name:

```text
image-1
```

Build Image:

```bash
docker build -t image-1 .
```

---

## Docker Containers

### Container A

```text
container-a
```

Port Mapping:

```text
4000:5000
```

### Container B

```text
container-b
```

Port Mapping:

```text
4001:5000
```

---

## Docker Volume

Volume Name:

```text
volume-a
```

Verify:

```bash
docker volume ls
docker volume inspect volume-a
```

---

## Docker Network

Network Name:

```text
network-a
```

Verify:

```bash
docker network ls
docker network inspect network-a
```

---

## Container Communication Test

Enter Container-A:

```bash
docker exec -it container-a bash
```

Ping Container-B:

```bash
ping container-b
```

Successful response confirms that both containers are connected to the same Docker network.

---

## Docker Compose Deployment

Start Services:

```bash
docker compose up -d
```

View Running Containers:

```bash
docker ps
```

View Logs:

```bash
docker compose logs
```

Stop Services:

```bash
docker compose down
```

Remove Services, Networks, and Volumes:

```bash
docker compose down -v
```

---

## Project Outcome

Successfully implemented:

* Docker Image Creation
* Multi-Container Deployment
* Docker Volumes
* Docker Networks
* Container-to-Container Communication
* Docker Compose Management

---
