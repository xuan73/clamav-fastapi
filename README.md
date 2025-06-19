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
docker compose up --build

### 3. Visit the web scanner
Open http://localhost:8000 and upload a file.

### 4. Try uploading a virus
Upload the file eicar.txt to see the scanner in action.
