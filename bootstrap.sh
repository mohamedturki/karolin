#!/bin/sh

MachineName="$1"

docker-machine create -d digitalocean --digitalocean-access-token=$DIGITALOCEAN_TOKEN \
                        --engine-env DB_NAME=postgres \
                        --engine-env DB_USER=postgres \
                        --engine-env DEBUG=False \
                        --engine-env DJANGO_SETTINGS_MODULE=karolin.settings.production \
                        --engine-env AWS_ACCESS=$AWS_ACCESS \
                        --engine-env AWS_SECRET=AWS_SECRET \
                        $MachineName
