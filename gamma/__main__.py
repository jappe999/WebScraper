from sys import argv
from colorama import init
from Gamma import Gamma

if __name__ == '__main__':
    # Initialize colorama
    init()

    HOST = 'localhost'
    PORT = str( 420 if len(argv) < 2 else argv[1] )

    gamma = Gamma('http://%s:%s' % (HOST, PORT, ))
    gamma.start()
