# Ultimate tic-tac-toe over the net

A version of [Ultimate tic-tac-toe](https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe) which you can play over a local network
or over the internet using my server (redboot.xyz:31001).

## Installation (Linux/macOS)

Dependencies: Java 8 (exaclty 8).

If you are running X11 display server (like most linux distros do), you may use dockerized version of the app, located in `docker/` folder.

```bash
git clone https://github.com/ly0va/net-tac-toe.git
cd net-tac-toe
```

## Usage

**Using local server**

This requires both clients and the server to be on the same *local* network.

1. Setup the server with `./server.py [host] [port]`.
   Default config is 0.0.0.0:31001.
2. Connect the first client with `./client.sh host port`.
   This will output the secret (a 16-byte string).
3. Connect the second client with `SECRET=<secret> ./client.sh host port`.

**Using redboot.xyz**

0. Server is already running at redboot.xyz:31001
1. Connect the first client with `./client.sh`
2. Connect the second client with `SECRET=<secret> ./client.sh`

Circle in the bottom-left corner denotes the color of your player.

Each turn, area where a move can be made is highlighted in yellow.

**Enjoy!**

## Screenshot

![Net-Tac-Toe](./board.jpg)


