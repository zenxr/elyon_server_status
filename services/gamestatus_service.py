import json
import redis

from config import configuration, games
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
   games = [game.to_dict() for game in games]
   for game in games:
      for server in game['servers']:
         server_address = server['ip_address']
         port = server['port']
         server['is_up'] = check_server_available(server_address, port)
   return json.dumps(games)

redis_store = _initialize_redis()
store_server_stats()
