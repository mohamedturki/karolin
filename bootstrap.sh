#!/bin/sh

MachineName="$1"

docker-machine create -d digitalocean --digitalocean-access-token=$DIGITALOCEAN_TOKEN \
                        --engine-env DB_NAME=postgres \
                        --engine-env DB_USER=postgres \
                        --engine-env DEBUG=False \
                        --engine-env DJANGO_SETTINGS_MODULE=karolin.settings.production \
                        --engine-env AWS_ACCESS=AKIAINZULEHYYVVXAMDA \
                        --engine-env AWS_SECRET=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 \
                        --engine-env SECRET_KEY=Vtz5T21QNi0jNoLqLtX3i0O6EfrnHN \
                        $MachineName
