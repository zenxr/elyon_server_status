from typing import DefaultDict
from flask import Flask, render_template
import os
import json

import configuration
from test_tcp_connection import check_server_available

app = Flask(__name__)
server_info = DefaultDict

def set_server_info_dict():
    global server_info
    with open('./server_info.json', 'r') as f:
        server_info = json.load(f)

def store_server_info(config_dict):
    global server_info
    with open('./server_info.json', 'w') as f:
        json.dump(config_dict)
    set_server_info_dict()

def get_server_status():
    print(server_info)
    server_statuses = {}
    for server_name in server_info['servers']:
        server_address = server_info['servers'][server_name]
        port = server_info['port']
        server_statuses[server_name.capitalize()] = check_server_available(server_address, port)
    return server_statuses

@app.route("/")
def index():
    status = get_server_status()
    print(status)
    return render_template('index.html', status = status)

if __name__ == '__main__':
    set_server_info_dict()
    app.run(host='0.0.0.0', port=configuration.app_port)