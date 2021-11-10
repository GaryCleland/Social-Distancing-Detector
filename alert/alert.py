from datetime import datetime
import hashlib
import fob.fob_data_collection as fob


class Alert:
    def __init__(self, camera, group_size, duration, location):
        self.camera = camera
        self.fob = fob.FobDataCollection(camera)
        self.fob_data = self.fob.get_student_count()
        self.location = location
        self.group_size = group_size
        self.duration = duration
        self.date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.classroom = self.get_class()
        self.module = self.get_module()
        self.course = self.get_course()
        # used to remove duplicates
        self.id = hashlib.sha1(str.encode(str(tuple(location))) + str.encode(str(group_size)) + str.encode(camera) +
                               str.encode(self.classroom) + str.encode(
                                datetime.today().strftime("%B %d, %Y"))).hexdigest()

    # retrieve class from DB based on what camera was used
    def get_class(self):
        # retrieve class
        return "test"

    # retrieve module from DB based on what camera was used
    def get_module(self):
        # retrieve module
        return "test"

    # retrieve course from DB based on what camera was used
    def get_course(self):
        # retrieve course
        return "test"
