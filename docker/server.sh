#!/bin/bash

# USAGE: ./server.sh [HOST] [PORT]

docker run -it --rm --net=host redboot/ntt-server:latest $1 $2
