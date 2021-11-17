

class SocialDistancingRules:

    def __init__(self, max_distance_apart=None, max_room_capacity=None, max_time_in_proximity=None, date_rule_created = None):
        self.max_distance_apart = max_distance_apart
        self.max_room_capacity = max_room_capacity
        self.max_time_in_proximity = max_time_in_proximity
        self.date_rule_created = date_rule_created

    # MaxDistanceApart is measured in meters
    def getMaxDistanceApart(self):
        return 2

    # MaxRoomCapacity is measured in number of people
    def getMaxRoomCapacity(self):
        return 30

    # MaxTimeInProximity is measured in minutes
    def getMaxTimeInProximity(self):
        return 15

    def getDateRuleCreated(self):
        return 'Jan 2021'

