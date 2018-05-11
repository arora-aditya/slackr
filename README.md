# slackr
[![Build Status](https://travis-ci.com/arora-aditya/slackr.svg?token=V7oVVD3ZsRcwAJiSN2sC&branch=master)](https://travis-ci.com/arora-aditya/slackr)

A command line clone of slack to learn about networks, sockets and ports!

## Current Functionality:
The server script: `src/server.py` accepts connections to it's socket from the client script: `src/client.py`

Control statements:
1. `/create <channel_name>`: Creates a channel if it doesn't exist already
2. `/join <channel_name>`: Join a pre-existing channel
3. `/list`: Lists all available channels

## Start slackr:
### Server:
`python3 src/server.py <port_number:optional>`

### Clients:
`python3 src/client.py <your_name> <hostname:optional> <port_number:optional>`

## Current Limitations:
- Max message size is limited to 200 characters:
[Expected fix: Use a unique key string to detect when messages are completely sent from clients]
- Limited to 5 open sockets for now, can be extended later to accommodate for more users
