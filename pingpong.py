def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return(cr)
    return start


@coroutine
def server():
    print "Starting game"
    while True:
        player_id, move = (yield)
        print "{} plays move {}".format(player_id, move)
        send_to_client(True)


@coroutine
def client():
    print "Starting client"
    count = 0
    send_to_server((1, count))
    while True:
        move_ahead = (yield)
        if move_ahead:
            print "Received go"
            count += 1
            send_to_server((1, count))
        else:
            print "Did not receive go"
        move_ahead = False

client_inst = client()
server_inst = server()


def send_to_client(obj):
    client_inst.send(obj)


def send_to_server(obj):
    server_inst.send(obj)

if __name__ == "__main__":
    from threading import Thread
    t1 = Thread(target=server)
    t2 = Thread(target=client)

    t2.start()
    t1.start()