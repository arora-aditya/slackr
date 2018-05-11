import random
import socket
import sys
import time
import os
from signal import SIGTERM
from subprocess import Popen, PIPE

sys.path.append(os.getcwd()+'/src')
import utils

SLEEP_SECONDS = 2

def pad_message(message):
  while len(message) < utils.MESSAGE_LENGTH:
    message += " "
  return message[:utils.MESSAGE_LENGTH]

class SplitMessages:
  def __init__(self, server_host, server_port):
    self.server_host = server_host
    self.server_port = server_port

  def send_split_message(self, client_socket, message):
    chars_sent = 0
    padded_message = pad_message(message)
    # Send random number of characters in the message.
    while chars_sent < utils.MESSAGE_LENGTH:
      last_char_to_send = random.randrange(chars_sent, utils.MESSAGE_LENGTH + 1)
      message_to_send = padded_message[chars_sent:last_char_to_send]
      if len(message_to_send) > 0:
        # print("Sending {} characters: {}".format(last_char_to_send - chars_sent, message_to_send))
        client_socket.sendall(message_to_send.encode())
        chars_sent = last_char_to_send

  def run(self):
    client_socket = socket.socket()
    try:
      server = Popen(["python", "src/server.py", str(port)])
      time.sleep(SLEEP_SECONDS)
      client_socket.connect((self.server_host, self.server_port))
      time.sleep(SLEEP_SECONDS)
    except:
      print(utils.CLIENT_CANNOT_CONNECT.format(self.server_host, self.server_port))
      return

    my_name = "SplitMessagesChatClient"
    # Send the server our name.
    self.send_split_message(client_socket, my_name)

    # Join a "split_messages" channel. This code assumes that the channel
    # already exists.
    self.send_split_message(client_socket, "/create split_messages")

    # Send the same message 10 times.
    message = ('This is just a test to see if the server can handle the load of exactly 200 characters but sent in pieces i.e. still have the ability to buffer them from cache. Excuse this string, trying to reach 200')
    for i in range(10):
      self.send_split_message(client_socket, message)
      time.sleep(1)
      
    # cleanly stop server by sending SIGTERM
    os.kill(server.pid, SIGTERM)

if __name__ == "__main__":
    if (len(sys.argv)) < 3:
        host, port = "localhost", 8000
        # print("Usage: python client_split_messages.py server_hostname server_port")
    else:
        host,port = sys.argv[1], int(sys.argv[2])

    chat_client = SplitMessages(host, port)
    sys.exit(chat_client.run())
