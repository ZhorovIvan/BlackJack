#main
from logging import raiseExceptions
from Croupier import croupier
from Frame import console,income
from Cards import cards

start_test = "Welcome to my new game!\nPlease, write income down"
incorrect_input = "You write incorrect value. Try again!"
choise_input_text = "You gotta choose next step (Stop or take)\n"
stop_word = "stop"
take_word = "take"
income_human = income.Income(0)
income_bot = income.Income(0)
new_consolee = console.Desk()
is_classic_game = True
desk_cards = cards.DeskOfCards()

def preparation():
    try:
        money = int(input())
        income_human.set_income(money)
        income_bot.set_income(money)
        user_choice =  str(input("Choose type of the game!\nClassic(yes) or not(no)\n"))
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
        

def game():
    try:
        humon_stop_step = False
        desk_cards.create_cards(is_classic_game)
        while(True):
            if not humon_stop_step:
                choice_humon = str(input(choise_input_text))
                if choice_humon.lower() == take_word:
                    new_consolee.clear_desk()
                    new_consolee.add_card(desk_cards.get_card())
                    print(new_consolee.print_all_cards())
                elif choice_humon.lower() == stop_word:
                    humon_stop_step = True
                else:
                    print(incorrect_input)
                    continue
            else:
                pass
                #I gotta write croupier bot code
    except Exception as e:
        print(e)


def main():
    try:
        print(start_test)
        preparation()
        while(True):
            game()
            if income_human.get_income() == 0:
                print("Bot win!")
            elif income_bot.get_income() == 0:
                print("You win!")   

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
