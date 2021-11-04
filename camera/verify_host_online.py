import os
import time
from threading import Thread


# Outputs whether or not the camera stream is down
# only in terminal for now
class LibVerifyHost:
    hostname = None
    stop_thread = None
    current_time = 0

    def __init__(self, camera_ip):
        self.host_name = camera_ip
        self.stop_thread = False

    # Start a daemon thread to check if host is down
    def Start(self):
        ping_thread = Thread(target=self.update, args=())
        ping_thread.daemon = True
        ping_thread.start()
        return self

    def update(self):
        while True:
            if self.stop_thread:
                print("ping thread stopped")
                return
            if time.clock() > self.current_time + 10:
                self.current_time = time.clock()
                response = os.system("ping -n 1 " + self.host_name)
                if response != 0:
                    print("host is down")

    def StopStreaming(self):
        self.stop_thread = True
