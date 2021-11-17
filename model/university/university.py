class University:

    def __init__(self, name=None, rooms=None, buildings=None, courses=None, lecturers=None):
        self.name = name
        self.rooms = rooms
        self.buildings = buildings
        self.courses = courses
        self.lecturers = lecturers

    def getName(self):
        return "Queen's University"

    def getRooms(self):
        return ['CSB 02.27', 'CSB 01.03', 'ASB 09.18']

    def getBuildings(self):
        return ['CSB', 'ASB', 'DKB']

    def getCourses(self):
        return ['EEECS', 'BIT', 'Biology']

    def getLecturers(self):
        return ['Barry', 'Blesson', 'Vahid']
