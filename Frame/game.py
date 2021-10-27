from logging import raiseExceptions
from Frame import console
from Cards import cards
import time
import configparser


config = configparser.ConfigParser()  
config.read("config.ini") 


incorrect_input = config["Game"]["incorrect_input"]
choise_input_text = config["Game"]["choise_input_text"] + "\n"
stop_word = "stop"
take_word = "take"
is_classic_game = True
desk_cards = cards.DeskOfCards()
new_human_desk = console.Desk()
new_bot_desk = console.Desk() 


def preparation():
    try:
        #search bug in the income class
        user_choice =  str(input(config["Game"]["type_of_game"] + "\n"))
        match user_choice:
            case "yes":
                is_classic_game = True
            case "no":
                is_classic_game = False
            case _:
                raise        
    except Exception as e:
        print(incorrect_input)
        preparation()
        

def move_in_game(who_move, messange):
    console.clear_desk()
    who_move.add_card(desk_cards.get_card())
    print(who_move.get_all_cards(messange))      


def round():
    humon_stop_step = False
    game = True
    try:
        desk_cards.create_cards(is_classic_game)
        while(game):
            if not humon_stop_step:
                choice_humon = str(input(choise_input_text))
                if choice_humon.lower() == take_word:
                    move_in_game(new_human_desk, "You")
                elif choice_humon.lower() == stop_word:
                    is_lose_human = new_human_desk.has_too_many_cards()
                    humon_stop_step = True
                else:
                    print(incorrect_input)
                    continue
            else:
                time.sleep(1)
                move_in_game(new_bot_desk, "Bot")
                game = new_bot_desk.is_enouth()
                is_lose_bot = new_bot_desk.has_too_many_cards()

        if is_lose_human and not is_lose_bot:
            return "Win"
        elif is_lose_bot and not is_lose_human:
            return "Lose"   
        elif is_lose_human and is_lose_bot or \
             new_bot_desk.get_ammount_cards() == new_human_desk.get_ammount_cards():
            return "Draw"   
    except Exception as e:
        print(e)
