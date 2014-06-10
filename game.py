from time import sleep
from random import randint


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return(cr)
    return start


class Server(object):
    def __init__(self):
        self.players = list()

    def add_players(self, players):
        count = 0
        for player in players:
            count += 1
            self.players.append(player)
            player.register_id(count)
            player.register_turn_mgr(self.start_game)
        self.leader = 1
        self.num_players = count
        print "Num players = {}".format(self.num_players)

    @coroutine
    def start_game(self):
        print "Starting game"
        while True:
            player_id, move = (yield)
            print "{} plays move {}".format(player_id, move)

THINK       = 0
CRAFTSMAN   = 1
LABORER     = 2
LEGIONARY   = 3
ARCHITECT   = 4
PATRON      = 5
MERCHANT    = 6
JACK        = 7


class Player(object):
    def __init__(self, name):
        self.name = name
        self.tm = None

    def register_id(self, player_id):
        self.player_id = player_id

    def register_turn_mgr(self, tm):
        self.tm = tm()

    def random_delay(self):
        sleep(randint(1, 10)/10.0)

    def precompute_turns(self, count):
        for ix in xrange(count):
            yield randint(THINK, JACK)

    def play(self):
        turns = self.precompute_turns(10)
        for turn in turns:
            self.tm.send((self.player_id, turn))
            self.random_delay()


if __name__ == "__main__":
    print "Hello"

    server = Server()
    p1 = Player("A")
    p2 = Player("B")
    p3 = Player("C")

    server.add_players([p1, p2, p3])
    from threading import Thread
    t1 = Thread(target=p1.play)
    t2 = Thread(target=p2.play)
    t3 = Thread(target=p3.play)

    t1.start()
    t2.start()
    t3.start()
