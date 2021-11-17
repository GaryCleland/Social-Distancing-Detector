import unittest
import model.university.course as Course
import pyodbc

course = Course.Course()

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=..\..\..\University.accdb;')


class TestGetMethods(unittest.TestCase):

    def testName(self):
        self.assertEqual(course.getName(), "EEECS")

    def testModules(self):
        self.assertEqual(course.getModules(), ['CSC4006', 'CSC2017', 'CSC1004'])

# Database retrieval tests

    def testDBName(self):
        cursor = conn.cursor()
        cursor.execute('select Course_name from Course')

        for row in cursor.fetchall():
            name = row[0]
            test_course = Course.Course(name=name)
        self.assertEqual(test_course.getName(), 'ELE')

    def testDBModules(self):
        cursor = conn.cursor()
        cursor.execute('select Modules from Course')

        for row in cursor.fetchall():
            modules = row[0].split(", ")
            test_course = Course.Course(modules=modules)
        self.assertEqual(test_course.getModules(), ['ELE1002', 'ELE4005', 'ELE2002'])


if __name__ == '__main__':
    unittest.main()
