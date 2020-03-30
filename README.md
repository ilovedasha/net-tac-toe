# Ultimate tic-tac-toe over the net

A version of [Ultimate tic-tac-toe](https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe) which you can play over a local network
or over the internet using my server (forkbenders.xyz:31001).

## Installation (Linux)

Dependencies: `java >= 1.8`, older versions may also work.

```bash
git clone https://github.com/lyova-potyomkin/net-tac-toe.git
cd net-tac-toe
./install.sh              # this downloads processing-py.jar
```

## Usage

**Using local server**

This requires both clients and the server to be on the same *local* network.

1. Setup the server with `./server.py [host] [port]`. 
   Default config is 0.0.0.0:31001.
2. Connect the first client with `./net-tac-toe.sh host port`.
   This will output the secret (a 16-byte string).
3. Connect the second client with `SECRET=<secret> ./net-tac-toe.sh host port`.

**Using forkbenders.xyz**

0. Server is already running at forkbenders.xyz:31001
1. Connect the first client with `./net-tac-toe.sh`
2. Connect the second client with `SECRET=<secret> ./net-tac-toe.sh`

Circle in the bottom-left corner denotes the color of your player.

Each turn, area where a move can be made is highlighted in yellow.

**Enjoy!**

## Screenshot

![Net-Tac-Toe](./board.jpg)


