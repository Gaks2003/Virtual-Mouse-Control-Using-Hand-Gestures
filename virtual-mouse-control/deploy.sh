#!/bin/bash

# Virtual Mouse Control Deployment Script

set -e

echo "Starting deployment process..."

# Build Docker image
echo "Building Docker image..."
docker build -t virtual-mouse-control:latest .

# Stop existing container if running
echo "Stopping existing container..."
docker stop virtual-mouse-control 2>/dev/null || true
docker rm virtual-mouse-control 2>/dev/null || true

# Run new container
echo "Starting new container..."
docker run -d \
  --name virtual-mouse-control \
  --privileged \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  -v /dev/video0:/dev/video0 \
  --device /dev/video0:/dev/video0 \
  virtual-mouse-control:latest

echo "Deployment completed successfully!"
echo "Container is running. Use 'docker logs virtual-mouse-control' to view logs."