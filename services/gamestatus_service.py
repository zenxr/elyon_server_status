import json
from typing import DefaultDict
import redis

from config import configuration
from util.test_tcp_connection import check_server_available

def _initialize_redis():
    # if REDIS_HOST is not set, try local connection
    if configuration.REDIS_HOST and configuration.REDIS_PORT:
        return redis.Redis(
            host=configuration.REDIS_HOST,
            port=configuration.REDIS_PORT
        )
    return redis.Redis()

def get_server_stats():
    return redis_store.get('server_stats').decode('utf-8')

def store_server_stats():
    server_stats = _fetch_server_stats()
    redis_store.mset({ 'server_stats' : server_stats})

def _fetch_server_stats():
    server_info = configuration.server_info
    server_stats = {}
    for server_area in server_info['servers']:
        server_stats[server_area] = {}
        for server_name in server_info['servers'][server_area]:
            server_address = server_info['servers'][server_area][server_name]
            port = server_info['port']
            server_stats[server_area][server_name.capitalize()] = check_server_available(server_address, port)
    return json.dumps(server_stats)

redis_store = _initialize_redis()
store_server_stats()
