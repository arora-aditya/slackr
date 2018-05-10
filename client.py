import socket
import sys
import select
from utils import CLIENT_CANNOT_CONNECT, CLIENT_SERVER_DISCONNECTED, CLIENT_MESSAGE_PREFIX, CLIENT_WIPE_ME, MESSAGE_LENGTH


class Client(object):

    def __init__(self, name, address, port):
        self.name = name
        self.address = address
        self.port = int(port)
        self.socket = socket.socket()

        try:
            self.socket.connect((self.address, self.port))
        except Exception as e:
            print(CLIENT_CANNOT_CONNECT.format(self.address, self.port))
            sys.exit()

        try:
            self.socket.send(self.name.ljust(MESSAGE_LENGTH))
        except Exception as e:
            sys.stdout.write(CLIENT_WIPE_ME)
            sys.stdout.write('\r' + CLIENT_SERVER_DISCONNECTED.format(self.address, self.port) + '\n')
            sys.exit()

        self.FD_LIST = [self.socket, sys.stdin]
        self.buffer = []

        sys.stdout.write(CLIENT_MESSAGE_PREFIX)
        sys.stdout.flush()

        while 1:

            ready_to_read, ready_to_write, in_error = select.select(self.FD_LIST, [], [])

            for fd in ready_to_read:
                if fd == self.socket:
                    data = self.socket.recv(MESSAGE_LENGTH)
                    if not data:
                        sys.stdout.write(CLIENT_WIPE_ME)
                        sys.stdout.write('\r' + CLIENT_SERVER_DISCONNECTED.format(self.address, self.port) + '\n')
                        sys.exit()
                    else:
                        msg_length = len(data)
                        output_str = ''
                        if self.buffer:
                            cached_msg = self.buffer.pop()
                            cached_len = len(cached_msg)
                            if cached_len + msg_length > MESSAGE_LENGTH:
                                output_str = cached_msg + data[:MESSAGE_LENGTH-cached_len]
                                self.buffer.append(data[MESSAGE_LENGTH-cached_len:])
                            elif cached_len + msg_length == MESSAGE_LENGTH:
                                output_str = cached_msg + data
                            else:
                                self.buffer.append(cached_msg + data)
                        else:
                            if msg_length < MESSAGE_LENGTH:
                                self.buffer.append(data)
                            else:
                                output_str = data

                        if output_str:
                            output_str = output_str.rstrip()
                            sys.stdout.write(CLIENT_WIPE_ME)
                            sys.stdout.write('\r'+output_str+'\n')
                            sys.stdout.write(CLIENT_MESSAGE_PREFIX)
                            sys.stdout.flush()
                else:
                    message = sys.stdin.readline()
                    try:
                        self.socket.send(message.ljust(MESSAGE_LENGTH))
                    except Exception as e:
                        sys.stdout.write(CLIENT_WIPE_ME)
                        sys.stdout.write('\r' + CLIENT_SERVER_DISCONNECTED.format(self.address, self.port) + '\n')
                        sys.exit()
                    sys.stdout.write(CLIENT_MESSAGE_PREFIX)
                    sys.stdout.flush()


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 4:
        print "Please supply a name, server address, and port."
        sys.exit()
    client = Client(args[1], args[2], args[3])
