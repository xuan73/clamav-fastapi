#!/bin/bash
docker ps | grep clamav-fastapi-single | awk '{print $1}' | xargs docker stop
