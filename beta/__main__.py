from sys import argv
from server import Server
from colorama import init


if __name__ == '__main__':
    # Initialize colorama
    init()

    PORT      = 420 if len(argv) < 2 else int(argv[1])
    NUM_LINKS = 10

    # Setup server
    server = Server('', PORT, NUM_LINKS)
    server.listen()
