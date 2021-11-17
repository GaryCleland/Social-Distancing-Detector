import unittest
import model.university.social_distancing_rules as SocialDistancingRules
import pyodbc

socialDistancingRules = SocialDistancingRules.SocialDistancingRules()

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\pault\Documents\CSC4008\University.accdb;')


class TestGetMethods(unittest.TestCase):

    def testMinSafeDistance(self):
        self.assertEqual(socialDistancingRules.getMinSafeDistance(), 2)

    def testMaxRoomCapacity(self):
        self.assertEqual(socialDistancingRules.getMaxRoomCapacity(), 30)

    def testMaxTimeInProximity(self):
        self.assertEqual(socialDistancingRules.getMaxTimeInProximity(), 15)

    def testDateRuleCreated(self):
        self.assertEqual(socialDistancingRules.getDateRuleCreated(), 'Jan 2021')

# Database retrieval tests

    def testDBMinSafeDistance(self):
        cursor = conn.cursor()
        cursor.execute('select Min_safe_distance from SocialDistancingRules')

        for row in cursor.fetchall():
            min_safe_distance = int(row[0])
            test_rules = SocialDistancingRules.SocialDistancingRules(min_safe_distance=min_safe_distance)
        self.assertEqual(test_rules.getMinSafeDistance(), 1)

    def testDBMaxRoomCapacity(self):
        cursor = conn.cursor()
        cursor.execute('select Max_room_capacity from SocialDistancingRules')

        for row in cursor.fetchall():
            max_room_capacity = int(row[0])
            test_rules = SocialDistancingRules.SocialDistancingRules(max_room_capacity=max_room_capacity)
        self.assertEqual(test_rules.getMaxRoomCapacity(), 35)

    def testDBMaxTimeInProximity(self):
        cursor = conn.cursor()
        cursor.execute('select Max_time_in_proximity from SocialDistancingRules')

        for row in cursor.fetchall():
            max_time_in_proximity = int(row[0])
            test_rules = SocialDistancingRules.SocialDistancingRules(max_time_in_proximity=max_time_in_proximity)
        self.assertEqual(test_rules.getMaxTimeInProximity(), 20)

    def testDBDateRuleCreated(self):
        cursor = conn.cursor()
        cursor.execute('select Date_rule_created from SocialDistancingRules')

        for row in cursor.fetchall():
            date_rule_created = row[0]
            test_rules = SocialDistancingRules.SocialDistancingRules(date_rule_created=date_rule_created)
        self.assertEqual(test_rules.getDateRuleCreated(), "Mar 2020")


if __name__ == '__main__':
    unittest.main()
