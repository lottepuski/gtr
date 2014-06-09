from time import sleep
from random import randint

def coroutine(func):
    def start(*args, **kwargs):
        cr=func(*args, **kwargs)
        cr.next()
        return(cr)
    return start

# Set 1
#@coroutine
#def grep(pattern):
    #print "Looking for {}".format(pattern)
    #while True:
        #line = (yield)
        #if pattern in line:
            #print line
# End Set 1


class Server(object):
    def __init__(self):
        self.players = list()

    def add_players(self, players):
        count = 1
        for player in players:
            self.players.append(player)
            self.player.register_id(count)
            self.player.register_turn_mgr(self.start_game)

    @coroutine
    def start_game(self):
        pass

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

    def register_id(self, player_id):
        self.player_id = player_id

    def register_turn_mgr(self, tm):
        self.tm = tm

    def random_delay(self):
        sleep(randint(1,10)/10.0)

    def precompute_turns(self, count):
        for ix in xrange(count):
            yield randint(THINK, JACK)

    def play(self):
        turns = self.precompute_turns(10)
        for turn in turns:
            self.tm.send(self.player_id, turn)
            self.random_delay()


if __name__=="__main__":
    print "Hello"

# Set 1
    #g = grep("python")
    #g.send("Yeah, but no, but yeah, but no")
    #g.send("A series of tubes")
    #g.send("python generators rock!")
    #g.send("A series of tubes")
    #g.send("python generators rock!")
# End Set 1


    server = Server()
    p1 = Player()
    p2 = Player()
    p3 = Player()
    server.add_players([p1, p2, p3])
