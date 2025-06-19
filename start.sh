#!/bin/bash

set -e

NETWORK_NAME="clamnet"
CLAM_CONTAINER="clamd"
APP_CONTAINER="clamav-fastapi"

echo "🔧 Ensuring Docker network '$NETWORK_NAME' exists..."
docker network inspect $NETWORK_NAME >/dev/null 2>&1 || docker network create $NETWORK_NAME

echo "🚀 Starting ClamAV container in background..."
docker run -d --rm \
    --network $NETWORK_NAME \
    --name $CLAM_CONTAINER \
    -p 3310:3310 \
    clamav/clamav:stable

echo "⏳ Waiting for ClamAV to start..."
sleep 10

if ! docker image inspect $APP_CONTAINER >/dev/null 2>&1; then
    echo "🔨 Building FastAPI image..."
    docker build -t $APP_CONTAINER .
fi

echo "🚀 Starting FastAPI container in background..."
docker run -d --rm \
    --network $NETWORK_NAME \
    --name web \
    -p 8000:8000 \
    -e CLAMD_HOST=$CLAM_CONTAINER \
    $APP_CONTAINER

echo "✅ Both containers are running."
echo "🌐 Visit: http://localhost:8000/docs"
