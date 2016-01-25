#!/bin/sh
#
# Build and push images to Docker registry.
#

echo -e '\e[32mGreen' "Building Web image for $1"
docker build -f web/Dockerfile -t mturki/karolin_web_$1 web
docker push mturki/karolin_web_$1

echo -e '\e[32mGreen' "Building Nginx image for $1"
docker build -f nginx/Dockerfile -t mturki/karolin_nginx_$1 nginx
docker push mturki/karolin_nginx_$1
