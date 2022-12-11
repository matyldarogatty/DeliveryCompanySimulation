class Driver:
    def __init__(self, name, vehicle, start_work):
        """
        :param name: (str)
        :param vehicle: (Vehicle)
        :param start_work: time driver starts working ex. '0710' (str)
        """
        self.name = name
        self.vehicle = vehicle
        self.current_package = None
        self.time = 300     #czas pracy w minutach
        self.driving_time = 0   #droga [czas] dowozu paczki
        self.start_work = start_work
        self.current_station = 'Station0'

    def is_ready(self, hour):
        """
        :param hour: current time (str) , ex. '0805'
        :return: bool
        """
        if int(hour[0:2]) > int(self.start_work[0:2]):
            return True
        elif int(hour[0:2]) == int(self.start_work[0:2]) and \
                int(hour[2:]) > int(self.start_work[2:]):
            return True
        return False

    def drive(self):  #jedna minuta jazdy
        self.time -= 1
        if self.busy():
            self.driving_time -= self.vehicle.get_speed()
            self.current_package.drive(self)

    def busy(self):
        return self.current_package is not None

    def start_next(self, package, time_left):
        """
        Driver starts delivering new package.

        :param package: (Package)
        :param time_left: time needed to cover the road (int)
        """
        self.current_package = package
        self.driving_time = time_left
        self.current_station = package.stat2  #ustawiam mu jak aktualną stację,
                                            #tę, na którą ma zawieść paczkę

