
import sqlite3


class Communicator(object):
    def __init__(self, f):
        self.first = f
        self.conn = sqlite3.connect(self.first, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()