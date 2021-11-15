from datetime import datetime
import hashlib
import fob.fob_data_collection as fob
from communicator import *

camera = None
group_size = None
duration = None
location = None
fob_data = None
date_time = None
comm = Communicator()


def sendToDatabase():
    """camera, group_size, duration, location, fob_data, date_time, get_room(camera),
    get_module(camera), get_course(camera)"""
    comm.sock.connect(('127.0.0.1', 51001))
    comm.send_msg(comm.sock, "replace")


def sendToWebApp():
    """camera, group_size, duration, location, fob_data, date_time, get_room(camera),
    get_module(camera), get_course(camera)"""
    comm.send_msg(comm.sock, b"replace")


def sendAlert(cam, size, time, loc):
    global camera, group_size, duration, location, fob_data, date_time
    camera = cam
    group_size = size
    duration = time
    location = loc
    fob_data = fob.FobDataCollection(camera).get_student_count()
    date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # used to remove duplicates
    alert_id = hashlib.sha1(str.encode(str(tuple(location))) + str.encode(str(group_size)) + str.encode(str(camera)) +
                            str.encode(datetime.today().strftime("%B %d, %Y"))).hexdigest()
    if not checkDuplicates(alert_id):
        sendToWebApp()
        # sendToDatabase()
    # print(cam, size, time, loc)


# retrieve room from DB based on what camera was used
def get_room():
    # retrieve room
    return "test"


# retrieve module from DB based on what camera was used
def get_module():
    # retrieve module
    return "test"


# retrieve course from DB based on what camera was used
def get_course():
    # retrieve course
    return "test"


def checkDuplicates(alert_id):
    """need to store ID in DB"""
    return False
