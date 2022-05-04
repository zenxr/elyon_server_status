
class Game(object):
   class GameServer(object):
      def __init__(self, name, ip_address, port, category = None):
         self.name = name
         self.ip_address = ip_address
         self.port = port
         self.category = category

      def to_dict(self):
         return {
            'name': self.name,
            'ip_address': self.ip_address,
            'port': self.port,
            'category': self.category
         }

   def __init__(self, name):
      self.name = name
      self.servers = []
      self.categories = []

   def add_server(self, name, ip_address, port, category = None):
      server = self.GameServer(name, ip_address, port, category)
      self.servers.append(server)
      if server.category:
         if not server.category in self.categories:
            self.categories.append(server.category)

   def to_dict(self):
      return {
         'name': self.name,
         'categories': self.categories,
         'servers': [server.to_dict() for server in self.servers]
      }


