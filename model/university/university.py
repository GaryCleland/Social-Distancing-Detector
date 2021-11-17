class University:

    def __init__(self, name=None, rooms=None, buildings=None, courses=None, lecturers=None):
        self.name = name
        self.rooms = rooms
        self.buildings = buildings
        self.courses = courses
        self.lecturers = lecturers

    def getName(self):
        if self.name is None:
            return "Queen's"
        else:
            return self.name

    def getRooms(self):
        if self.rooms is None:
            return ['CSB 02.27', 'CSB 01.03', 'DKB 09.18']
        else:
            return self.rooms

    def getBuildings(self):
        if self.buildings is None:
            return ['CSB', 'ASB', 'ECIT']
        else:
            return self.buildings

    def getCourses(self):
        if self.courses is None:
            return ['EEECS', 'BIT', 'Biology']
        else:
            return self.courses

    def getLecturers(self):
        if self.lecturers is None:
            return ['Barry', 'Blesson', 'Vahid']
        else:
            return self.lecturers
