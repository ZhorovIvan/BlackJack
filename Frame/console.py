import os

class Desk:

    jack = "Jack"
    queen = "Queen"
    king = "King"
    ace = "Ace"

    def __init__(self):
        self.cards = []
        self.amount_cards = 0


    def get_ammount_cards(self):
        return self.amount_cards


    def add_amount(self, card):
        match card:
            case self.jack:
                self.amount_cards += 2
            case self.queen:
                self.amount_cards += 3
            case self.king:
                self.amount_cards += 4
            case self.ace:
                self.amount_cards += 11
            case _:
                self.amount_cards += int(card)


    def has_too_many_cards(self):
        return self.amount_cards > 21


    def add_card(self,card):
        self.cards.append(card)
        self.add_amount(card[0])


    def get_all_cards(self, who_is_moved):
        return who_is_moved + " cards - " + str(self.cards).replace("[", "").replace("]", "") +\
                "\nSum " + who_is_moved + " cards equals - " + str(self.amount_cards)


    def is_enouth(self):
        return self.amount_cards <= 15            


def clear_desk():
    os.system('cls' if os.name == 'nt' else 'clear')