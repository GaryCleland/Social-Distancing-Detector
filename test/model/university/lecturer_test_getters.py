import unittest
import model.university.lecturer as Lecturer

lecturer = Lecturer.Lecturer()


class TestGetMethods(unittest.TestCase):

    def testStaffNumber(self):
        self.assertEqual(lecturer.getStaffNumber(), "Test40203145")

    def testModules(self):
        self.assertEqual(lecturer.getModules(), ['CSC4006', 'CSC4005', 'CSC4008'])


if __name__ == '__main__':
    unittest.main()
