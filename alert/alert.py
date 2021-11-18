from datetime import datetime
import hashlib

import communicator
import fob.fob_data_collection as fob
import model.university.university as md
import model.university.lecturer as lec

camera = None
group_size = None
duration = None
location = None
fob_data = None
date_time = None
alert_id = None
comm = communicator.Communicator()
university = md.University()
lecturer = lec.Lecturer()


def sendToDatabase():
    comm.cursor.execute("INSERT OR IGNORE INTO Alert(Id, Camera, Group_size, Fob_data, Date_time, Duration, "
                        "Room, Module, University, Lecturer) VALUES (?,?,?,?,?,?,?,?,?,?)",
                        (alert_id, camera, group_size, fob_data, date_time, duration, get_room(),
                         get_module(), get_university(), get_lecturer()))

    comm.conn.commit()


def sendToWebApp():
    """camera, group_size, duration, fob_data, date_time, get_room(camera),
    get_module(camera), get_course(camera)"""


def sendAlert(cam, size, time):
    global camera, group_size, duration, location, fob_data, date_time, alert_id
    camera = cam
    group_size = size
    duration = time
    fob_data = fob.FobDataCollection(camera).get_student_count()
    date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # used to remove duplicates
    alert_id = hashlib.sha1(str.encode(str(group_size)) + str.encode(str(camera)) +
                            str.encode(datetime.today().strftime("%B %d, %Y"))).hexdigest()
    # TODO: implement check Dupes
    sendToDatabase()


# retrieve room from DB based on what camera was used
def get_room():
    # retrieve room
    return university.getRooms()[camera]


# retrieve module from DB based on what camera was used
def get_module():
    # retrieve module
    return lecturer.getModules()[camera]


# retrieve course from DB based on what camera was used
def get_lecturer():
    # retrieve course
    return university.getLecturers()[camera]


def get_university():
    return university.getName()


def checkDuplicates(alert_id):
    """need to store ID in DB"""
    return False
