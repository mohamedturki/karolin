#!/bin/sh
#
# Build and push images to Docker registry.
#

docker build -f web/Dockerfile -t mturki/karolin_web web
docker push mturki/karolin_web

docker build -f nginx/Dockerfile -t mturki/karolin_nginx nginx
docker push mturki/karolin_nginx
