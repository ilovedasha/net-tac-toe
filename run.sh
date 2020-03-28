#!/bin/sh

# USAGE: ./run.sh [SECRET]
# To play, run clients with matching secrets

[ -z "$1" ] && \
    java -jar processing-py.jar client/client.pyde || \
    NETTACTOE_SECRET="$1" java -jar processing-py.jar client/client.pyde



