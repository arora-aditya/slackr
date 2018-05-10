MESSAGE_LENGTH = 200
CLIENT_CANNOT_CONNECT = "Unable to connect to {0}:{1}"
CLIENT_SERVER_DISCONNECTED = "Server at {0}:{1} has disconnected"
CLIENT_MESSAGE_PREFIX = "[Me] "
CLIENT_WIPE_ME = "\r    "
SERVER_INVALID_CONTROL_MESSAGE = \
  "{0} is not a valid control message. Valid messages are /create, /list, and /join."
SERVER_NO_CHANNEL_EXISTS = "No channel named {0} exists. Try '/create {0}'?"
SERVER_JOIN_REQUIRES_ARGUMENT = "/join command must be followed by the name of a channel to join."
SERVER_CLIENT_JOINED_CHANNEL = "{0} has joined"
SERVER_CLIENT_LEFT_CHANNEL = "{0} has left"
SERVER_CHANNEL_EXISTS = "Room {0} already exists, so cannot be created."
SERVER_CREATE_REQUIRES_ARGUMENT = \
  "/create command must be followed by the name of a channel to create"
SERVER_CLIENT_NOT_IN_CHANNEL = \
  "Not currently in any channel. Must join a channel before sending messages."
def printError(e, newline = False):
    if newline:
        print()
    print('\x1b[1;31;40m' + 'ERROR: \t' + str(e) + '\x1b[0m')
def printLog(log, newline = False):
    if newline:
        print()
    print('\x1b[1;32;40m' + 'LOG: \t' + log + '\x1b[0m')
def printMsg(msg):
    print('\x1b[1;33;40m' + 'MSG: \t' + msg + '\x1b[0m')
