from datetime import datetime
import hashlib


class Alert:
    def __init__(self, violations, camera, fob_data, location=None):
        self.violations = violations
        self.camera = camera
        self.fob_data = fob_data
        self.location = location
        self.date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.classroom = self.get_class()
        self.module = self.get_module()
        self.course = self.get_course()
        # used to remove duplicates
        self.id = hashlib.sha1(str.encode(violations) + str.encode(camera) + str.encode(self.classroom) +
                               str.encode(datetime.today().strftime("%B %d, %Y"))).hexdigest()

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
