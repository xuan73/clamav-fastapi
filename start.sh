#!/bin/bash
docker build -t clamav-fastapi-single .
docker run --rm -p 8000:8000 clamav-fastapi-single
