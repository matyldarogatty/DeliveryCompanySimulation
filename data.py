from structures.graph import Graph
from package import Package
from structures.stack import Stack


class Data:
    '''This class makes objects as Stack of Packages
    and connection Graph.
    Everything is created in function __init__().'''

    def __init__(self, map_file, packages_file):
        """
        First: makes all packages, then sorts them.
        Second: creates connetion graph with stations.
        """
        self.g = Graph()
        self.packages_lst = []
        self.packages_stack = Stack()

        # tworzę objekty - paczki
        with open(packages_file, 'r') as p:
            num_packages = int(p.readline())
            for i in range(num_packages):
                package_data = p.readline().strip()
                lst = package_data.split()  #lista z danymi paczki [id, ...]
                package = Package(int(lst[0]), lst[1], lst[2], int(lst[3]))
                self.packages_lst.append(package)
        # insertion sort - sortuje paczki wzgl godziny, od której są dostępne
        # i dodaję je do stosu
        for i in range(1, len(self.packages_lst)):
            j = i
            while j > 0 and int(self.packages_lst[j - 1].av) <= int(self.packages_lst[j].av):
                self.packages_lst[j], self.packages_lst[j - 1] = self.packages_lst[j - 1], self.packages_lst[j]
                j -= 1
        for package in self.packages_lst:
            self.packages_stack.push(package)

        #tworzę graf złożony ze stacji i ich odległości
        with open(map_file, 'r') as m:
            stations = []
            num_stations = int(m.readline())
            for _ in range(num_stations):   #dodaję stacje do grafu
                station_name = m.readline().strip()
                stations.append(station_name)
                self.g.add_vertex(station_name)
            matrix_dist = []
            for _ in range(num_stations):
                distances = m.readline().split()  #distances to lista odległości z i-tej stacji
                matrix_dist.append(distances)     #do pozostałych -> macierz
                assert len(distances) == num_stations
            for k in range(num_stations):
                for j in range(num_stations):
                    self.g.add_edge(stations[k], stations[j], int(matrix_dist[k][j]))
                    self.g.add_edge(stations[j], stations[k], int(matrix_dist[j][k]))

    def get_packages(self):
        return self.packages_stack

    def get_graph(self):
        return self.g


if __name__ == '__main__':
    data = Data('map.txt', 'packages.txt')
    print(data)
    for i in data.g:
        print(i)
    print(data.get_packages().size())
    for i in range(24):
        #print(data.get_packages().peek().id)
        print(data.get_packages().pop().id)
