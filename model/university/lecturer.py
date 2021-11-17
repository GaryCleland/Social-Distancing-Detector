

class Lecturer:
    def __init__(self, staff_number=None, modules=None):
        self.staff_number = staff_number
        self.modules = modules

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
