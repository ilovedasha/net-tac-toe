#!/bin/sh

# USAGE: [SECRET=<secret>] ./net-tac-toe.sh [HOST] [PORT]
# To play, run clients with matching secrets

HOST="$1" PORT="$2" java -jar processing-py.jar client/client.pyde



