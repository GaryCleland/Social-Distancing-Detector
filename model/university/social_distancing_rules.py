

class SocialDistancingRules:

    def __init__(self, min_safe_distance=None, max_room_capacity=None, max_time_in_proximity=None, date_rule_created=None):
        self.min_safe_distance = min_safe_distance
        self.max_room_capacity = max_room_capacity
        self.max_time_in_proximity = max_time_in_proximity
        self.date_rule_created = date_rule_created

    # MinSafeDistance is measured in meters
    def getMinSafeDistance(self):
        if self.min_safe_distance is None:
            return 2
        else:
            return self.min_safe_distance

    # MaxRoomCapacity is measured in number of people
    def getMaxRoomCapacity(self):
        if self.max_room_capacity is None:
            return 30
        else:
            return self.max_room_capacity

    # MaxTimeInProximity is measured in minutes
    def getMaxTimeInProximity(self):
        if self.max_time_in_proximity is None:
            return 15
        else:
            return self.max_time_in_proximity

    def getDateRuleCreated(self):
        if self.date_rule_created is None:
            return 'Jan 2021'
        else:
            return self.date_rule_created

