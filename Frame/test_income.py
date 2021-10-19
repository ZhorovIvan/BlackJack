import unittest
import income

class TestIncome(unittest.TestCase):

    def test_bigger_value(self):
        with self.assertRaises(Exception):
            income.Income(130)


    def test_smaller_value(self):
        with self.assertRaises(Exception):
            income.Income(-100)


    def test_not_digit(self):
        with self.assertRaises(Exception):
            income.Income("d")


    def test_bool_value(self):
        with self.assertRaises(Exception):
            income.Income(True)


    def test_set_string_value(self):
        income_test = income.Income(10)
        with self.assertRaises(Exception): 
            income_test.set_income(True)


    def test_set_string_value(self):
        income_test = income.Income(10)
        with self.assertRaises(Exception): 
            income_test.set_income("33")
    

        