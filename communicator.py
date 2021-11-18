
import sqlite3


class Communicator(object):
    def __init__(self):
        self.conn = sqlite3.connect('Alert.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()