# elyon_server_status

Simple web application that displays the availability of a game's servers.

# Requirements

- docker and docker-compose

- cd into project directory and `./docker_run.sh` to run the app.

# About

docker-compose defines two containers:
- web - the python web application
- redis - for data store

The web app is in flask and utilizes celery to schedule a single process that checks server availability. The web application grabs the server statuses from the redis store rather than sending out requests per client.

## ToDo

- Schedule updates in webapp to periodically refresh server status client-side automatically
