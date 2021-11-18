import unittest
import model.university.module as Module
import university_communicator

module = Module.Module()

conn = university_communicator.Communicator()


class TestGetMethods(unittest.TestCase):

    def testDefaultModuleCode(self):
        self.assertEqual(module.getModuleCode(), "CSC4008")

    def testDefaultRooms(self):
        self.assertEqual(module.getRooms(), ['CSB 02/27', 'CSB 01/16', 'DKB 0G/334'])

    def testDefaultLecturer(self):
        self.assertEqual(module.getLecturer(), 'Barry')

# Database retrieval tests

    def testDBModuleCode(self):
        cursor = conn.cursor.execute('select Module_code from Module')

        for row in cursor.fetchall():
            module_code = row[0]
            test_module = Module.Module(module_code=module_code)
        self.assertEqual(test_module.getModuleCode(), "CSC4005")

    def testDBLecturer(self):
        cursor = conn.cursor.execute('select Lecturer from Module')

        for row in cursor.fetchall():
            lecturer = row[0]
            test_module = Module.Module(lecturer=lecturer)
        self.assertEqual(test_module.getLecturer(), 'Blesson')

    def testDBRooms(self):
        cursor = conn.cursor.execute('select Rooms from Module')

        for row in cursor.fetchall():
            rooms = row[0].split(", ")
            test_module = Module.Module(rooms=rooms)
        self.assertEqual(test_module.getRooms(), ['ASB 09/18', 'CSB 02/27', 'DKB 0G/124'])


if __name__ == '__main__':
    unittest.main()
