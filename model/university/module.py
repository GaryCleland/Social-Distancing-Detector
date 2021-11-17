

class Module:

    def __init__(self, module_code=None, lecturer=None, rooms=None, course=None):
        self.module_code = module_code
        self.lecturer = lecturer
        self.rooms = rooms
        self.course = course

    def getModuleCode(self):
        if self.module_code is None:
            return 'CSC4008'
        else:
            return self.module_code

    def getLecturer(self):
        if self.lecturer is None:
            return 'Barry'
        else:
            return self.lecturer

    def getRooms(self):
        if self.rooms is None:
            return ['CSB 02.27', 'CSB 01.16', 'DKB 03.34']
        else:
            return self.rooms

    def getCourse(self):
        if self.course is None:
            return 'EEECS'
        else:
            return self.course
        
