
from enum import Enum

from util.host_validator import assert_valid_host

class GameServerCheckType(Enum):
   TCP = 1
   UDP = 2

class Game(object):
   class GameServer(object):
      def __init__(self, name, host, port, category = None):
         assert_valid_host(host)
         self.name = name
         self.host = host
         self.port = port
         self.category = category
         self.is_alive = None

      def to_dict(self):
         return {
            'name': self.name,
            'host': self.host,
            'port': self.port,
            'category': self.category,
            'is_alive': self.is_alive
         }

   def __init__(self, name : str, checkmethod: GameServerCheckType):
      self.name = name
      self.checkmethod = checkmethod
      self.servers = []
      self.categories = []

   def add_server(self, name, host, port, category = None):
      '''Add a server to a Game

      Attributes:
         name: Server name
         host: Server host, or IP address
         port: Port to be monitored
         (optional) category: Categorization within this Game, e.g.: FFA, CTF, etc
      '''
      server = self.GameServer(name, host, port, category)
      self.servers.append(server)
      if server.category:
         if not server.category in self.categories:
            self.categories.append(server.category)

   def to_dict(self):
      return {
         'name': self.name,
         'categories': self.categories,
         'checkmethod': self.checkmethod.name,
         'servers': [server.to_dict() for server in self.servers]
      }

