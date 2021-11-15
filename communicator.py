import socket


class Communicator(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('127.0.0.1', 51000))

    def send_msg(self, sock, msg):
        sock.send(msg)
