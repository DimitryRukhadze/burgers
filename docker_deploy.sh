#!/bin/bash

set -e
git pull
docker-compose up -d --build
docker exec burgers-web-1 python manage.py migrate --noinput
docker exec burgers-web-1 python manage.py collectstatic --noinput
git_hash=$(git rev-parse --short HEAD)
comments=$(git log -1 --pretty=%B)
echo "Finished Deploying!"