import os


#make only script

class Desk:

    def __init__(self):
        self.my_cards = []
        self.bot_cards = []
        self.amount_humon_cards = 0
        pass


    def add_amount(self, digit):
        self.amount_humon_cards += digit


    def has_too_many_cards():
        return self.amount_humon_cards > 21


    def print_all_cards(self, sum_bot, sum_humon):
        print(self.my_cards + sum_humon + "\n" +
                self.bot_cards + sum_bot)


    def clear_desk(self):
        os.system('cls' if os.name == 'nt' else 'clear')