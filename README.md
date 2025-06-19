# ClamAV FastAPI Virus Scanner

This project runs a web-based virus scanner using ClamAV and FastAPI, fully containerized with Docker.

## 🚀 Quick Start

Make sure you have [Docker](https://www.docker.com/products/docker-desktop/) installed.

### 1. Clone this project

```bash
git clone https://github.com/xuan73/clamav-fastapi.git
cd clamav-fastapi
```

### 2. Start both FastAPI + ClamAV
#### Build with docker-compose

```bash
docker compose up --build
```

#### Build with docker, run both services in the same Docker Network

```bash
chmod +x start.sh
./start.sh
```

### 3. Visit the web scanner

Open http://localhost:8000 and upload a file.

### 4. Try uploading a virus

Upload the file eicar.txt to see the scanner in action.

## 🚫 Known Issues & Fixes

### ClamAV fails to start / clamd exits

- Ensure clamd.conf is correct
- Run freshclam before clamd (done in Dockerfile)

### freshclam exits too fast in Supervisor

- It's better to run freshclam once during build or manually at runtime, not via Supervisor

## 🛠️ Customization

You can:

- Replace the HTML upload form with your own branding
- Add scan history tracking
- Connect to a remote ClamAV instance

## 🌐 Deployment

This is ideal for self-hosting or internal security tools. It can also be deployed to:

- EC2 or any cloud VM
- Portainer / Docker Swarm
- Kubernetes (as a single pod)

## 🌟 Credits

- Created by xuan73
- Blog post: Building a Web-Based Virus Scanner Using ClamAV and FastAPI

## 🔧 License

- MIT License