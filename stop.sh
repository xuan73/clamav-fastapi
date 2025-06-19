#!/bin/bash

echo "🛑 Stopping containers..."
docker stop clamd web 2>/dev/null || true

echo "🧹 Cleaning up Docker network (clamnet)..."
docker network rm clamnet 2>/dev/null || true

echo "✅ Done."
