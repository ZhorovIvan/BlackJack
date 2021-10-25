import os

class Desk:

    jack = "Jack"
    queen = "Queen"
    king = "King"
    ace = "Ace"

    def __init__(self):
        self.human_cards = []
        self.amount_humon_cards = 0


    def add_amount(self, card):
        match card:
            case self.jack:
                self.amount_humon_cards += 2
            case self.queen:
                self.amount_humon_cards += 3
            case self.king:
                self.amount_humon_cards += 4
            case self.ace:
                self.amount_humon_cards += 11
            case _:
                self.amount_humon_cards += int(card)


    def has_too_many_cards(self):
        return self.amount_humon_cards > 21


    def print_all_cards(self):
        return (str(self.amount_humon_cards))


    def clear_desk(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def add_card(self,card):
            self.human_cards.append(card)
            self.add_amount(card[0])
