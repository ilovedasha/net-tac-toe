#!/usr/bin/env bash

# USAGE: [SECRET=<secret>] ./net-tac-toe.sh [HOST] [PORT]
# To play, run clients with matching secrets

if ! [ -f processing-py.jar ]; then
    case "$(uname -s)" in
        Linux*)     platform="linux64" ;;
        Darwin*)    platform="macosx"  ;;
        *)          echo "Unsupported platform"; exit 1 ;;
    esac

    curl -qL "http://py.processing.org/processing.py-$platform.tgz" | tar xzf - --wildcards '*/processing-py.jar'
    mv processing.py*/processing-py.jar .
    rmdir processing.py*
fi

HOST="${1:-redboot.xyz}" PORT="${2:-31001}" java -jar processing-py.jar client/client.pyde



