class Server(object):
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def start_game(self):
        """ Starts the game state machine
        """
        pass
