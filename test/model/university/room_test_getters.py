import unittest
import model.university.room as Room

room = Room.Room()


class TestGetMethods(unittest.TestCase):

    def testName(self):
        self.assertEqual(room.getRoomNumber(), "02.27")

    def testModules(self):
        self.assertEqual(room.getModules(), ['CSC4005', 'CSC1036', 'CSC3004', 'CSC2011'])

    def testBuilding(self):
        self.assertEqual(room.getBuilding(), 'CSB')

    def testMaximumCapacity(self):
        self.assertEqual(room.getMaximumCapacity(), 100)


if __name__ == '__main__':
    unittest.main()
