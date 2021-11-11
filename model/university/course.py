

class Course:

    def __init__(self, name=None, modules=None):
        self.name = name
        self.modules = modules

    def getName(self):
        return 'EEECS'

    def getModules(self):
        return ['CSC4006', 'CSC2017']

