import unittest
import model.university.room as Room
import pyodbc

room = Room.Room()

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\pault\Documents\CSC4008\University.accdb;')


class TestGetMethods(unittest.TestCase):

    def testDefaultName(self):
        self.assertEqual(room.getRoomNumber(), "02.27")

    def testDefaultModules(self):
        self.assertEqual(room.getModules(), ['CSC4005', 'CSC1036', 'CSC3004'])

    def testDefaultBuilding(self):
        self.assertEqual(room.getBuilding(), 'CSB')

    def testDefaultMaximumCapacity(self):
        self.assertEqual(room.getMaximumCapacity(), 100)

    def testFullRoomNumber(self):
        self.assertEqual(room.getFullRoomName(), "CSB 02.27")

# Database retrieval tests

    def testDBRoomNumber(self):
        cursor = conn.cursor()
        cursor.execute('select Room_number from Room')

        for row in cursor.fetchall():
            room_number = row[0]
            test_room = Room.Room(room_number=room_number)
        self.assertEqual(test_room.getRoomNumber(), "01.16")

    def testDBBuilding(self):
        cursor = conn.cursor()
        cursor.execute('select Building from Room')

        for row in cursor.fetchall():
            building = row[0]
            test_room = Room.Room(building=building)
        self.assertEqual(test_room.getBuilding(), 'DKB')

    def testDBModules(self):
        cursor = conn.cursor()
        cursor.execute('select Modules from Room')

        for row in cursor.fetchall():
            modules = row[0].split(", ")
            test_room = Room.Room(modules=modules)
        self.assertEqual(test_room.getModules(), ['CSC4005', 'CSC1036', 'ELE1004'])

    def testDBMaxCapacity(self):
        cursor = conn.cursor()
        cursor.execute('select Maximum_capacity from Room')

        for row in cursor.fetchall():
            max_capacity = int(row[0])
            test_room = Room.Room(maximum_capacity=max_capacity)
        self.assertEqual(test_room.getMaximumCapacity(), 150)

    def testDBFullRoomNumber(self):
        cursor = conn.cursor()
        cursor.execute('select Room_number, Building from Room')

        for row in cursor.fetchall():
            room_number = row[0]
            building = row[1]
            test_room = Room.Room(room_number=room_number, building=building)
        self.assertEqual(test_room.getFullRoomName(), 'DKB 01.16')


if __name__ == '__main__':
    unittest.main()
