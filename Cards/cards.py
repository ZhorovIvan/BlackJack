from typing import Final


class DeskOfCards():
    desk_cards = []
    KIND_OF_CARDS : Final = 13

    ClUB : Final = "Club"
    DIAMOND : Final = "Diamont"
    HEART : Final = "Heart"
    SPADE : Final = "Spade"

    JACK : Final = "Jack"
    QUEEN : Final = "Queen"
    KING : Final = "King"
    ACE : Final = "Ace"


    #There are four kind of cards.
    #clubsDeskOfCards
    #diamonds
    #hearts
    #spades
    def __init__(self):
        pass


    def add_to_desk(self, rank):
        desk_cards.append((rank, ClUB))
        desk_cards.append((rank, DIAMOND))
        desk_cards.append((rank, HEART))
        desk_cards.append((rank, SPADE))


    def create_cards(self, cards_type = "Classic"):
        start_position = 2

        if cards_type == "Classic":
            start_position = 6

        for i in range(start_position, KIND_OF_CARDS):
            if i < 11:
                add_to_desk(i)
            else:
                match i:
                    case "11":
                        add_to_desk(JACK)
                    case "12":
                        add_to_desk(QUEEN)
                    case "13":
                        add_to_desk(KING)
                    case "14":
                        add_to_desk(ACE)

        def print_desk(self):
            print(self.desk_cards)

f = DeskOfCards()
f.create_cards()
