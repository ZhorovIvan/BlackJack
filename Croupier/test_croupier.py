import croupier
import unittest

class TestCroupier(unittest.TestCase):

    def setUp(self):
        self.A = croupier.Croupier("Ivan")


    def test_get_name(self):
        self.assertEqual(self.A.get_name(),"Ivan")


    def test_get_amout(self):
        self.assertEqual(self.A.get_amount(),0)    
