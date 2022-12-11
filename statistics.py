from matplotlib.pyplot import *


class Statistics:
    """
    This class is making file or drawing diagram
    based on data added by function add_stat().
    """
    def __init__(self, date):
        """
        :param date: dd_mm_yyyy (str)
        """
        self.date = date
        self.stat = dict()      # klucz to imię kierowcy, wartość to
                                # lista złożona z id dowiezionych paczek

    def write(self):
        with open(self.date+'_stat.txt', 'w') as u:
            u.write(self.date)
            for driver in self.stat:
                u.write('\n')

                u.write(driver + ':' + str(self.stat[driver]))

    def add_stat(self, driver, package):
        """
        :param driver: name (str)
        :param package: id (str)
        """
        if driver in self.stat:
            self.stat[driver].append(package)
        else:
            self.stat[driver] = [package]

    def return_file(self):
        """
        Making file.
        """
        self.write()

    def draw(self):
        """
        This function is drawing bar chart.
        """
        x, y = [], []
        for d, lst in self.stat.items():
            x.append(d)
            y.append(len(lst))
        bar(x, y)
        show()

