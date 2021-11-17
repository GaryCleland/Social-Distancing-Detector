import unittest
import model.university.module as Module
import pyodbc

module = Module.Module()

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\pault\Documents\CSC4008\University.accdb;')


class TestGetMethods(unittest.TestCase):

    def testModuleCode(self):
        self.assertEqual(module.getModuleCode(), "CSC4008")

    def testRooms(self):
        self.assertEqual(module.getRooms(), ['CSB 02.27', 'CSB 01.16', 'DKB 03.34'])

    def testCourse(self):
        self.assertEqual(module.getCourse(), 'EEECS')

    def testLecturer(self):
        self.assertEqual(module.getLecturer(), 'Barry')

# Database retrieval tests

    def testDBModuleCode(self):
        cursor = conn.cursor()
        cursor.execute('select Module_code from Module')

        for row in cursor.fetchall():
            module_code = row[0]
            test_module = Module.Module(module_code=module_code)
        self.assertEqual(test_module.getModuleCode(), "CSC4005")

    def testDBLecturer(self):
        cursor = conn.cursor()
        cursor.execute('select Lecturer from Module')

        for row in cursor.fetchall():
            lecturer = row[0]
            test_module = Module.Module(lecturer=lecturer)
        self.assertEqual(test_module.getLecturer(), 'Blesson')

    def testDBRooms(self):
        cursor = conn.cursor()
        cursor.execute('select Rooms from Module')

        for row in cursor.fetchall():
            rooms = row[0].split(", ")
            test_module = Module.Module(rooms=rooms)
        self.assertEqual(test_module.getRooms(), ['ASB 09.18', 'CSB 02.27', 'DKB 01.24'])

    def testDBCourse(self):
        cursor = conn.cursor()
        cursor.execute('select Course from Module')

        for row in cursor.fetchall():
            course = row[0]
            test_module = Module.Module(course=course)
        self.assertEqual(test_module.getCourse(), 'ELE')


if __name__ == '__main__':
    unittest.main()
