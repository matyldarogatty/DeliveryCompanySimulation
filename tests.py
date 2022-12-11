import unittest
from deliverycompany import *


class TestDeliveryCompany(unittest.TestCase):
    """ This class tests DeliveryCompany"""

    def setUp(self):
        self.bike = Vehicle(0.3)
        self.tesla = Vehicle(2)
        self.driver1 = Driver('Johny Test', self.tesla, '1300')
        self.driver2 = Driver('Phoebe', self.bike, '0800')
        self.company = DeliveryCompany('map.txt', 'packages.txt', [self.driver1, self.driver2], '07_02_2021')

    def test(self):
        with self.assertRaises(ValueError):
            Vehicle(10)
        self.assertEqual(self.company.describe_route('Station2', 'Station3'), (['Station2-Station3: 12'], 12))
        self.assertEqual(self.company.packages.size(), 11)
        before = self.company.packages.size()
        self.company.simulate_without_print()
        after = self.company.packages.size()
        self.assertFalse(before == after)
        self.assertTrue(before > after)


if __name__ == '__main__':
    unittest.main()

