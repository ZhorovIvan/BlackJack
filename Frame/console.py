
class Desk:

#I can init croupier module here.


    amount_humon_cards = 0
    my_cards = []
    bot_cards = []

    def __init__(self):
        pass


    def add_amount(self, digit):
        self.amount_humon_cards += digit


    def has_too_many_cards():
        return self.amount_humon_cards > 21


    def print_all_cards(self, sum_bot, sum_humon):
        print(self.my_cards + sum_humon + "\n" +
                self.bot_cards + sum_bot)
