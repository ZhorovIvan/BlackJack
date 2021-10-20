import random


class DeskOfCards():

    count_cards = 15

    #There are four kind of cards.
    #clubsDeskOfCards
    #diamonds
    #hearts
    #spades

    club = "Club"
    diamont = "Diamont"
    heart = "Heart"
    spade = "Spade"

    jack = "Jack"
    queen = "Queen"
    king = "King"
    ace = "Ace"


    def __init__(self):
        self.desk_cards = []
        pass


    def add_to_desk(self, rank):
        self.desk_cards.append((rank, self.club))
        self.desk_cards.append((rank, self.diamont))
        self.desk_cards.append((rank, self.heart))
        self.desk_cards.append((rank, self.spade))


    def create_cards(self, is_classic = True):
        start_position = 2

        if is_classic == True:
            start_position = 6

        for i in range(start_position, self.count_cards):
            if i < 11:
                self.add_to_desk(i)
            else:
                match i:
                    case 11:
                        self.add_to_desk(self.jack)
                    case 12:
                        self.add_to_desk(self.queen)
                    case 13:
                        self.add_to_desk(self.king)
                    case 14:
                        self.add_to_desk(self.ace)


    def get_card(self):
        index_card = random.randrange(len(self.desk_cards))
        card = self.desk_cards[index_card]
        self.desk_cards.pop(index_card)
        return card


    def get_all_cards(self):
        return self.desk_cards