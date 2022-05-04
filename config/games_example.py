from entities.game_entities import Game

# add your games using methodology below
# a game can have multiple servers, and servers can belong to categories

elyon = Game(name='Elyon')
elyon.add_server(nname='a', ip_address='127.0.0.1', port='80', category='North America')
elyon.add_server(name='b', ip_address='127.0.0.1', port='80', category='North America')
elyon.add_server(name='c', ip_address='127.0.0.1', port='80', category='Europe')
elyon.add_server(name='d', ip_address='127.0.0.1', port='80', category='Europe')

raiderz = Game(name='Raiderz')
raiderz.add_server(name='primary', ip_address='127.0.0.1', port='80', port='80')
raiderz.add_server(name='secondary', ip_address='127.0.0.1', port='80')

games = [elyon, raiderz]