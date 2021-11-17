import unittest
import model.university.university as University
import pyodbc

university = University.University()

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=..\..\..\University.accdb;')


class TestGetMethods(unittest.TestCase):

    def testDefaultName(self):
        self.assertEqual(university.getName(), "Queen's")

    def testDefaultRooms(self):
        self.assertEqual(university.getRooms(), ['CSB 02/27', 'CSB 01/03', 'DKB 0G/118'])

    def testDefaultBuildings(self):
        self.assertEqual(university.getBuildings(), ['CSB', 'ASB', 'ECIT'])

    def testDefaultLecturers(self):
        self.assertEqual(university.getLecturers(), ['Dr. Barry McCollum', 'Dr. Blesson Varghese', 'Dr. Jesus Martinez del Rincon'])

# Database retrieval tests

    def testDBName(self):
        cursor = conn.cursor()
        cursor.execute('select university_name from University')

        for row in cursor.fetchall():
            name = row[0]
            uni = University.University(name=name)
        self.assertEqual(uni.getName(), "Queen's University")

    def testDBRooms(self):
        cursor = conn.cursor()
        cursor.execute('select rooms from University')

        for row in cursor.fetchall():
            rooms = row[0].split(", ")
            uni = University.University(rooms=rooms)
        self.assertEqual(uni.getRooms(), ['CSB 02/27', 'CSB 01/13', 'ASB 09/18'])

    def testDBBuildings(self):
        cursor = conn.cursor()
        cursor.execute('select buildings from University')

        for row in cursor.fetchall():
            buildings = row[0].split(", ")
            uni = University.University(buildings=buildings)
        self.assertEqual(uni.getBuildings(), ['CSB', 'ASB', 'DKB'])

    def testDBLecturers(self):
        cursor = conn.cursor()
        cursor.execute('select lecturers from University')

        for row in cursor.fetchall():
            lecturers = row[0].split(", ")
            uni = University.University(lecturers=lecturers)
        self.assertEqual(uni.getLecturers(), ['Dr. Barry McCollum', 'Dr. Blesson Varghese', 'Dr.Dave Cutting'])


if __name__ == '__main__':
    unittest.main()
