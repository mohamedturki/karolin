#!/bin/sh
#
# Build and push images to Docker registry.
#

echo -e "Building Web image for $1\e[32mGreen"
docker build -f web/Dockerfile -t mturki/karolin_web_$1 web
docker push mturki/karolin_web_$1

echo -e "Building Nginx image for $1\e[32mGreen"
docker build -f nginx/Dockerfile -t mturki/karolin_nginx_$1 nginx
docker push mturki/karolin_nginx_$1
