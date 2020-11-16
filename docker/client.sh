#!/bin/bash

# USAGE: [SECRET=<secret>] ./client.sh [HOST] [PORT]
# To play, run clients with matching secrets

export HOST=${1:-redboot.xyz}
export PORT=${2:-31001}

docker run --rm -it --volume "$HOME/.Xauthority:/root/.Xauthority:rw" \
    --env DISPLAY --env SECRET --env HOST --env PORT --net=host \
    redboot/ntt-client:latest


