import unittest
import model.university.university as University

university = University.University()


class TestGetMethods(unittest.TestCase):

    def testName(self):
        self.assertEqual(university.getName(), "Queen's University")

    def testRooms(self):
        self.assertEqual(university.getRooms(), ['CSB 02.27', 'CSB 01.03', 'ASB 09.18'])

    def testBuildings(self):
        self.assertEqual(university.getBuildings(), ['CSB', 'ASB', 'DKB'])

    def testCourses(self):
        self.assertEqual(university.getCourses(), ['EEECS', 'BIT'])

    def testLecturers(self):
        self.assertEqual(university.getLecturers(), ['Barry', 'Blesson', 'Vahid'])


if __name__ == '__main__':
    unittest.main()
