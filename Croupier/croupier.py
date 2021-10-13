
class Croupier:

    amount_of_curds = 0

    jack = "Jack"
    queen = "Queen"
    king = "King"
    ace = "Ace"


    def __init__(self,name):
        self.name = name


    def is_enouth(self):
        if self.amount_of_curds < 15:
            return True
        return False


    def add_card(self, card):
        if str(card[0]).isnumeric():
            self.amount_of_curds += card[0]
        else:
            match card[0]:
                case self.jack:
                    self.amount_of_curds += 1
                case self.queen:
                    self.amount_of_curds += 2
                case self.king:
                    self.amount_of_curds += 3
                case self.ace:
                    self.amount_of_curds += 11


    def get_amount(self):
        return self.amount_of_curds


    def get_name(self):
        return self.name
