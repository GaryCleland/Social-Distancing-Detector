

class Room:
    def __init__(self, room_number=None, building=None, modules=None, maximum_capacity=None):
        self.room_number = room_number
        self.building = building
        self.modules = modules
        self.maximum_capacity = maximum_capacity

    def getRoomNumber(self):
        return "02.27"

    def getBuilding(self):
        return "CSB"

    def getModules(self):
        return ['CSC4005', 'CSC1036', 'CSC3004']

    def getMaximumCapacity(self):
        return 100

