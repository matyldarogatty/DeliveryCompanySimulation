from data import Data
from dijkstra import Dijkstra
from driver import Driver
from vehicle import Vehicle
from clock import Clock
from statistics import Statistics


class DeliveryCompany:
    def __init__(self, map_file, package_file, drivers, date):
        """
        Creates objects: Data, Clock and Statistics.
        Attribute m is needed to tests.
        :param map_file:
        :param package_file:
        :param drivers: list of drivers
        :param date: dd_mm_yyyy (str)
        """
        self.data = Data(map_file, package_file)
        self.drivers = drivers           #lista kierowców
        self.packages = self.data.get_packages()  #stos paczek
        self.conection_graph = self.data.get_graph()
        self.clock = Clock()
        self.stat = Statistics(date)
        self.m = True

    def shortest_path(self, station1, station2):
        """
        Finding the best route from station1 to station2
        :param station1: where package is (str)
        :param station2: destination (str)
        :return: list
        """
        dij = Dijkstra(self.conection_graph)
        dij.dijkstra(station1)
        return dij.traverse(station2)

    def describe_route(self, station1, station2):
        """
        :param station1: start (str)
        :param station2: destination (str)
        :return: (route (list), distance (int))  (tuple)
        """
        path = self.shortest_path(station1, station2)
        route = []
        total_time = 0
        for i in range(len(path) - 1):
            stat1 = self.conection_graph.get_vertex(path[i])
            stat2 = self.conection_graph.get_vertex(path[i + 1])
            time = stat1.get_weight(stat2)
            total_time += time
            route.append(f"{stat1.id}-{stat2.id}: {time}")
        return route, total_time

    def tick(self):
        """ What happens in 1 minute."""
        self.clock.tick()
        for driver in self.drivers:
            if driver.current_package is not None:
                driver.drive()
                if driver.current_package.is_delivered():
                    if self.m: print("{}: delivered package {:0>10} to {}".format(driver.name, driver.current_package.id,
                                                                       driver.current_package.stat2))
                    driver.current_package = None

    def simulate(self):                         #a = 0
        """
        This function is a simulation of one work day. It takes 10h.
        """
        for cur_minute in range(600):
            if not self.packages.is_empty():    #jeśli są jakieś paczki w kolejce
                for driver in self.drivers:
                    if not driver.is_ready(self.clock.get_time()):
                        continue
                    if self.packages.is_empty():          ### Jeśli będą dodawane nowe: continue
                        if self.m: print('All packages delivered.')
                        break
                    package = self.packages.peek()     #weź pierwszą ze stosu
                    (route, total_time) = self.describe_route(package.stat1, package.stat2)
                    if int(package.av) <= int(self.clock.get_time()) and driver.time >= \
                            total_time and not driver.busy():  #jeśli paczka jest dostępna a
                                            #kurier ma wystarczająco dużo czasu i nie jest zajety
                        if driver.current_station == package.stat1:   #jeśli znajduje się na tej stacji
                            package = self.packages.pop()      #usuwam tą paczkę ze stosu
                            driver.start_next(package, total_time)
                            package.start_driving(total_time)
                            self.stat.add_stat(driver.name, str(package.id))   #a += 1
                            if self.m:
                                self.clock.print_time()
                                print("{}: started delivering package {:0>10}, time needed: {}min".format(driver.name,
                                                    package.id, round(total_time / driver.vehicle.get_speed())))


                        #Jeśli kurier musi pojechać po paczke:
                        else:
                            (route1, total_time1) = self.describe_route(driver.current_station, package.stat1)
                            driver.time -= driver.vehicle.get_speed() * total_time1
                            package = self.packages.pop()  # usuwam tą paczkę z kolejki
                            driver.start_next(package, total_time)
                            package.start_driving(total_time)
                            self.stat.add_stat(driver.name, str(package.id))   #a += 1
                            if self.m:
                                self.clock.print_time()
                                print(route1)
                                print("{}: started delivering package {:0>10}, time needed: {}min".format(driver.name,
                                                                    package.id, round(total_time / driver.vehicle.get_speed())))
                    continue
                self.tick()    #print(a)

    def simulate_without_print(self):
        self.m = False
        self.simulate()

    def make_stat(self):
        """ This function calls function return_file() in class Statistics."""
        self.stat.return_file()

    def show_stat(self):
        """ This function calls function draw() in class Statistics."""
        self.stat.draw()


if __name__ == '__main__':
    audi = Vehicle(1.1)
    scouter = Vehicle(0.85)
    opel = Vehicle(1)
    bike = Vehicle(0.3)
    tesla = Vehicle(2)
    driver1 = Driver('Melanie', audi, '0800')
    driver2 = Driver('Joe', audi, '0800')
    driver3 = Driver('Morthy', bike, '1200')
    driver4 = Driver('Estelle', tesla,'1200')
    driver5 = Driver('Devorah', opel, '1400')
    driver6 = Driver('Mark', opel, '1400')
    driver7 = Driver('Joey', opel, '0900')
    driver8 = Driver('Phoebe', opel, '1000')
    company = DeliveryCompany('map.txt', 'packages.txt', [driver1, driver2, driver3,
                            driver4, driver5, driver6, driver7, driver8], '20_05_2021')
    #print(company.describe_route('Station0', 'Station1'))
    #print(company.describe_route('Station1', 'Station0'))
    #print(len(data.get_packages()))
    #company.simulate_without_print()
    company.simulate()
    company.make_stat()
    company.show_stat()


