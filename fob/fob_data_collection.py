
class FobDataCollection:
    def __init__(self, camera_id):
        self.camera_id = camera_id

# returns number of students in the class
# mimics collection of fob data
    def get_student_count(self):
        if self.camera_id == 0:
            return 15
        elif self.camera_id == 1:
            return 20
        elif self.camera_id == 2:
            return 25
        elif self.camera_id == 3:
            return 30
