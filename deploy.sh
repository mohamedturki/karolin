#!/bin/sh

docker-compose build
docker-compose -f production up -d
