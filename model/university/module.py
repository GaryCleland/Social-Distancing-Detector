

class Module:

    def __init__(self, module_code=None, lecturer=None, rooms=None, course=None):
        self.module_code = module_code
        self.lecturer = lecturer
        self.rooms = rooms
        self.course = course

    def getModuleCode(self):
        return 'CSC4008'

    def getLecturer(self):
        return 'Barry'

    def getRooms(self):
        return ['CSB 02.27', 'CSB 01.16', 'DKB 03.34']

    def getCourse(self):
        return 'EEECS'

