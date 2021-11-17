import unittest
import model.university.social_distancing_rules as SocialDistancingRules

socialDistancingRules = SocialDistancingRules.SocialDistancingRules()


class TestGetMethods(unittest.TestCase):

    def testMaxDistanceApart(self):
        self.assertEqual(socialDistancingRules.getMaxDistanceApart(), 2)

    def testMaxRoomCapacity(self):
        self.assertEqual(socialDistancingRules.getMaxRoomCapacity(), 30)

    def testMaxTimeInProximity(self):
        self.assertEqual(socialDistancingRules.getMaxTimeInProximity(), 15)

    def testDateRuleCreated(self):
        self.assertEqual(socialDistancingRules.getDateRuleCreated(), 'Jan 2021')


if __name__ == '__main__':
    unittest.main()
