from entities.game_entities import Game, GameServerCheckType

# add your games using methodology below
# a game can have multiple servers, and servers can belong to categories

elyon = Game(name='Elyon', checkmethod=GameServerCheckType.TCP)
elyon.add_server(name='a', host='127.0.0.1', port=80, category='North America')
elyon.add_server(name='b', host='127.0.0.1', port=80, category='North America')
elyon.add_server(name='c', host='127.0.0.1', port=80, category='Europe')
elyon.add_server(name='d', host='127.0.0.1', port=80, category='Europe')

raiderz = Game(name='Raiderz', checkmethod=GameServerCheckType.RAW_SOCKET)
raiderz.add_server(name='primary', host='127.0.0.1', port=80)
raiderz.add_server(name='secondary', host='127.0.0.1', port=80)

games = [elyon, raiderz]
