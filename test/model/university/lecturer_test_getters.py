import unittest
import model.university.lecturer as Lecturer
import pyodbc

lecturer = Lecturer.Lecturer()

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=..\..\..\University.accdb;')


class TestGetMethods(unittest.TestCase):

    def testStaffNumber(self):
        self.assertEqual(lecturer.getStaffNumber(), 40203145)

    def testModules(self):
        self.assertEqual(lecturer.getModules(), ['CSC4006', 'CSC4005', 'CSC4008'])

# Database retrieval tests

    def testDBStaffNumber(self):
        cursor = conn.cursor()
        cursor.execute('select Staff_number from Lecturer')

        for row in cursor.fetchall():
            staff_number = int(row[0])
            test_lecturer = Lecturer.Lecturer(staff_number=staff_number)
        self.assertEqual(test_lecturer.getStaffNumber(), 40203055)

    def testDBModules(self):
        cursor = conn.cursor()
        cursor.execute('select Modules from Lecturer')

        for row in cursor.fetchall():
            modules = row[0].split(", ")
            test_lecturer = Lecturer.Lecturer(modules=modules)
        self.assertEqual(test_lecturer.getModules(), ['CSC3005', 'CSC4005', 'ELE3021'])


if __name__ == '__main__':
    unittest.main()
