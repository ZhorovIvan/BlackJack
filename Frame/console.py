import os


#make only script

class Desk:

    def __init__(self):
        self.my_cards = []
        self.bot_cards = []
        self.amount_humon_cards = 0


    def add_amount(self, digit):
        self.amount_humon_cards += digit


    def has_too_many_cards(self):
        return self.amount_humon_cards > 21


    def print_all_cards(self, sum_bot, sum_humon):
        return (self.my_cards + sum_humon + "\n" +
                self.bot_cards + sum_bot)


    def clear_desk(self):
        os.system('cls' if os.name == 'nt' else 'clear')