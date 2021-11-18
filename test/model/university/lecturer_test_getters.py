import unittest
import model.university.lecturer as Lecturer
import university_communicator

lecturer = Lecturer.Lecturer()

comm = university_communicator.Communicator()


class TestGetMethods(unittest.TestCase):

    def testDefaultName(self):
        self.assertEqual(lecturer.getName(), 'Dr. Barry McCollum')

    def testDefaultStaffNumber(self):
        self.assertEqual(lecturer.getStaffNumber(), 40203145)

    def testDefaultModules(self):
        self.assertEqual(lecturer.getModules(), ['CSC4006', 'CSC4005', 'CSC4008'])

# Database retrieval tests

    def testDBName(self):
        cursor = comm.cursor.execute('select Lecturer_name from Lecturer')

        for row in cursor.fetchall():
            name = row[0]
            test_lecturer = Lecturer.Lecturer(name=name)
        self.assertEqual(test_lecturer.getName(), 'Dr. Blesson Varghese')

    def testDBStaffNumber(self):
        cursor = comm.cursor.execute('select Staff_number from Lecturer')

        for row in cursor.fetchall():
            staff_number = int(row[0])
            test_lecturer = Lecturer.Lecturer(staff_number=staff_number)
        self.assertEqual(test_lecturer.getStaffNumber(), 40203055)

    def testDBModules(self):
        cursor = comm.cursor.execute('select Modules from Lecturer')

        for row in cursor.fetchall():
            modules = row[0].split(", ")
            test_lecturer = Lecturer.Lecturer(modules=modules)
        self.assertEqual(test_lecturer.getModules(), ['CSC3005', 'CSC4005', 'ELE3021'])


if __name__ == '__main__':
    unittest.main()
