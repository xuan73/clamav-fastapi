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
docker network create clamnet
docker build -t clamav-fastapi .
docker run --platform=linux/amd64 --rm --name clamd -p 3310:3310 clamav/clamav:stable
docker run --rm -p 8000:8000 --env CLAMD_HOST=clamd clamav-fastapi
```
We can also run
```bash
./start.sh
```
and
```bash
./stop.sh
```
to make this process easier

#### If ClamAV runs on a different host or VM, then:
Set CLAMD_HOST to the IP or DNS of that server.
Make sure ClamAV’s port 3310 is open to the FastAPI machine (via firewall/security group).
Run FastAPI like:
```bash
docker run --rm -p 8000:8000 \
  -e CLAMD_HOST=12.34.56.78 \
  -e CLAMD_PORT=3310 \
  clamav-fastapi
```

### 3. Visit the web scanner
Open http://localhost:8000 and upload a file.

### 4. Try uploading a virus
Upload the file eicar.txt to see the scanner in action.
