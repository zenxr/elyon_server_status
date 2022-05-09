import json
import redis

from config import configuration
from config import games as games_config
from entities.game_entities import Game, GameServerCheckType
from util.server_checks import check_tcp_available, check_udp_available

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
    games = games_config.games
    for game in games:
       _check_game_servers(game)
    server_stats = json.dumps([game.serialize() for game in games])
    redis_store.mset({ 'server_stats' : server_stats})

def _check_game_servers(game: Game):
   for server in game.servers:
      if game.checkmethod == GameServerCheckType.TCP:
         server.is_alive = check_tcp_available(server.host, server.port)
      elif game.checkmethod == GameServerCheckType.RAW_SOCKET:
         server.is_alive = check_udp_available(server.host, server.port)
      else:
         raise NotImplementedError(f'{game.checkmethod.name} is not yet supported.')

redis_store = _initialize_redis()
store_server_stats()
