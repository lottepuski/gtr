import sys
from server import start_server
from player import create_player


def main():
    """Runs the server and client state machines
    """
    server = start_server()
    p1 = create_player()
    p2 = create_player()
    p3 = create_player()

    server.add_player(p1)
    server.add_player(p2)
    server.add_player(p3)

    server.start_game()

if __name__ == "__main__":
    sys.exit(main())
