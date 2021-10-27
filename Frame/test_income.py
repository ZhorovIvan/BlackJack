import unittest
import point

class TestPoint(unittest.TestCase):

    def test_bigger_value(self):
        with self.assertRaises(Exception):
            point.Point(130)


    def test_smaller_value(self):
        with self.assertRaises(Exception):
            point.Point(-100)


    def test_not_digit(self):
        with self.assertRaises(Exception):
            point.Point("d")


    def test_bool_value(self):
        with self.assertRaises(Exception):
            point.Point(True)


    def test_set_string_value(self):
        income_test = point.Point(10)
        with self.assertRaises(Exception): 
            income_test.set_income(True)


    def test_set_string_value(self):
        income_test = point.Point(4)
        with self.assertRaises(Exception): 
            income_test.set_income("33")
    

        