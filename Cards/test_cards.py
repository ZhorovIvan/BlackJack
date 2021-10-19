import unittest
import cards

class TestCards(unittest.TestCase):
    

    def test_get_big_desk(self):
        classic_desk = cards.DeskOfCards()
        classic_desk.create_cards(False)
        self.assertEqual(len(classic_desk.get_all_cards()), 52)

    
    def test_get_classic_desk(self):
        classic_desk = cards.DeskOfCards()
        classic_desk.create_cards()
        self.assertEqual(len(classic_desk.get_all_cards()), 32)  
