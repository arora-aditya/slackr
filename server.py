import socket
import sys
from utils import  MESSAGE_LENGTH, SERVER_INVALID_CONTROL_MESSAGE, SERVER_NO_CHANNEL_EXISTS,\
 SERVER_JOIN_REQUIRES_ARGUMENT, SERVER_CLIENT_JOINED_CHANNEL,\
   SERVER_CLIENT_LEFT_CHANNEL, SERVER_CHANNEL_EXISTS,\
    SERVER_CREATE_REQUIRES_ARGUMENT, SERVER_CLIENT_NOT_IN_CHANNEL

args = sys.argv

class BasicServer(object):

    def __init__(self, port):
        self.socket = socket.socket()
        self.socket.bind(("", int(port)))
        self.socket.listen(5)

    def start(self):
        try:
            while True:
                (new_socket, address) = self.socket.accept()
                msg = new_socket.recv(1024)
                tmp = msg
                while tmp:
                    tmp = new_socket.recv(1024)
                    msg += tmp
                print(msg.decode())
        except KeyboardInterrupt:
            print()
            print("Caught interrupt, stopping server")
            sys.exit()


if __name__ == '__main__':
    if len(args) <= 2:
        port = 8000
    elif len(args) == 2:
        port = args[1]
    else:
        port = args[1]
        print("Ignoring other arguments, starting server on port {}".format(str(port)))
    print('\x1b[1;32;40m' + 'Starting server, Ctrl+C to stop' + '\x1b[0m')
    server = BasicServer(port)
    server.start()
