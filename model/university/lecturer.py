

class Lecturer:
    def __init__(self, name=None, staff_number=None, modules=None):
        self.name = name
        self.staff_number = staff_number
        self.modules = modules

    def getName(self):
        if self.name is None:
            return 'Dr. Barry McCollum'
        else:
            return self.name

    def getStaffNumber(self):
        if self.staff_number is None:
            return 40203145
        else:
            return self.staff_number

    def getModules(self):
        if self.modules is None:
            return ['CSC4006', 'CSC4005', 'CSC4008']
        else:
            return self.modules
