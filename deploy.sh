#!/bin/sh

docker-compose -f production.yml build;
docker-compose -f production.yml up -d;
