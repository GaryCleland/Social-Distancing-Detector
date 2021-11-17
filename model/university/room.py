

class Room:
    def __init__(self, room_number=None, building=None, modules=None, maximum_capacity=None):
        self.room_number = room_number
        self.building = building
        self.modules = modules
        self.maximum_capacity = maximum_capacity

    def getRoomNumber(self):
        if self.room_number is None:
            return "02.27"
        else:
            return self.room_number

    def getBuilding(self):
        if self.building is None:
            return "CSB"
        else:
            return self.building

    def getModules(self):
        if self.modules is None:
            return ['CSC4005', 'CSC1036', 'CSC3004']
        else:
            return self.modules

    def getMaximumCapacity(self):
        if self.maximum_capacity is None:
            return 100
        else:
            return self.maximum_capacity

    def getFullRoomName(self):
        return self.getBuilding() + " " + self.getRoomNumber()

