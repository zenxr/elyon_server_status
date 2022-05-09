# Server Status Application

Simple web application that displays the availability of a game's servers.

# Requirements

- docker and docker-compose
- `docker-compose up -d` to run the application in detached mode

## Configuration

Clone `config/games_example.py` to `config/games.py` and edit configuration to configure which game servers to monitor.

# About

docker-compose defines two containers:
- web - the python web application
- redis - for data store

The web app is in flask and utilizes celery to schedule a single process that checks server availability. The web application grabs the server statuses from the redis store rather than sending out requests per client.

## ToDo

- [x] Schedule updates in webapp to periodically refresh server status client-side automatically
	- [ ] Full page refresh currently, instead use Ajax or similar to only refresh required DOM elements

- [x] Only supports checking connections via TCP. Add support for UDP or custom methods.
- [ ] Update UI
- [x] Support hostnames rather than just IP for more reliability of games that have changing IPs.

