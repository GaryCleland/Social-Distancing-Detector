import unittest
import model.university.course as Course

course = Course.Course()


class TestGetMethods(unittest.TestCase):

    def testName(self):
        self.assertEqual(course.getName(), "EEECS")

    def testModules(self):
        self.assertEqual(course.getModules(), ['CSC4006', 'CSC2017'])


if __name__ == '__main__':
    unittest.main()
