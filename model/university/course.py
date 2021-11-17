

class Course:

    def __init__(self, name=None, modules=None):
        self.name = name
        self.modules = modules

    def getName(self):
        if self.name is None:
            return 'EEECS'
        else:
            return self.name

    def getModules(self):
        if self.modules is None:
            return ['CSC4006', 'CSC2017', 'CSC1004']
        else:
            return self.modules

