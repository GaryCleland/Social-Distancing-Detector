import pickle
import struct
import socket


class Communicator(object):
    def __init__(self):
        self.sock = socket.socket()

    def send_msg(self, sock, msg):
        msg_pickle = pickle.dumps(msg)
        sock.sendall(struct.pack(">I", len(msg_pickle)))
        sock.sendall(msg_pickle)

    def recv_msg(self, sock):
        msg_len = struct.unpack(">I", sock.recv(4))[0]
        msg = sock.recv(msg_len, socket.MSG_WAITALL)
        return pickle.loads(msg)
