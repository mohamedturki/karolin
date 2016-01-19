#!/bin/sh

docker-compose build;
docker-compose -f production.yml up -d;
