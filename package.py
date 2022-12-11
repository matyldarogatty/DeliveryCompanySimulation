class Package:
    def __init__(self, id, station1, station2, available):
        """
        :param id: max len = 10 (str)
        :param station1: (str)
        :param station2: (str)
        :param available: ex. '0730'(str)
        """
        self.id = id
        self.stat1 = station1
        self.stat2 = station2
        self.av = available
        self.time_left = 0

    def start_driving(self, time_left):
        """
        :param time_left: time needed from station1 to station2 (int)
        """
        self.time_left = time_left

    def drive(self, driver):
        self.time_left -= 1 * driver.vehicle.get_speed()

    def is_delivered(self):
        return self.time_left <= 0

