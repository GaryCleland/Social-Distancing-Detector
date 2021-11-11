import unittest
import model.university.module as Module

module = Module.Module()


class TestGetMethods(unittest.TestCase):

    def testModuleCode(self):
        self.assertEqual(module.getModuleCode(), "CSC4008")

    def testRooms(self):
        self.assertEqual(module.getRooms(), ['CSB 02.27'])

    def testCourse(self):
        self.assertEqual(module.getCourse(), 'EEECS')

    def testLecturer(self):
        self.assertEqual(module.getLecturer(), 'Barry')


if __name__ == '__main__':
    unittest.main()
