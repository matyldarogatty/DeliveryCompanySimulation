class Clock:
    """
    This class represents clock.
    """
    def __init__(self, start_hour='0800'):
        """
        The default starting time is 8:00.
        :param start_hour: (str) ex. '0730'
        """
        self.hour = int(start_hour[0:2])
        self.minutes = int(start_hour[2:4])

    def tick(self):
        """
        This function is adding 1 minute to current time.
        """
        if self.minutes < 60:
            self.minutes += 1
        else:
            self.hour += 1
            self.minutes = 0

    def get_time(self):
        hour = str(self.hour)
        minutes = str(self.minutes)

        if len(str(self.hour)) < 2:
            hour = '0' + str(self.hour)
        if len(str(self.minutes)) < 2:
            minutes = '0' + str(self.minutes)

        return hour + minutes

    def print_time(self):
        time = self.get_time()
        time = time[0:2] + ':' + time[2:]
        print(time)


if __name__ == '__main__':
    time = Clock()
    print(time.get_time())
    for _ in range(77):
        time.tick()
    print(time.hour)
    print(time.minutes)
    print(time.get_time())