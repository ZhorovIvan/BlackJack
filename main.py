#main
from logging import raiseExceptions
from Croupier import croupier
from Frame import console,income
from Cards import cards

start_test = "Welcome to my new game!"
incorrect_input = "You write incorrect value. Try again!"
choise_input_text = "You gotta choose next step (Stop or take)\n"
stop_word = "stop"
take_word = "take"
income_human = income.Income(0)
income_bot = income.Income(0)
new_consolee = console.Desk()
is_classic_game = True


def preparation():
    try:
        money = int(input())
        income_human.set_income(money)
        income_bot.set_income(money)
        is_classic_game = bool(input("Choose type of the game!\nClassic(yes) or not(no)\n"))
        #I can use here lumbda expretion
    except Exception as e:
        print(incorrect_input)
        preparation()
        

def game():
    try:
        humon_stop_step = False

        while(True):
            if not humon_stop_step:
                choiceHumon = str(input(choise_input_text))
                if choiceHumon.lower() == stop_word:
                    new_consolee.clear_desk()

                elif choiceHumon.lower() == take_word:
                    pass
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
            deskCards = cards.DeskOfCards(is_classic_game)
            game()
            if income_human.get_income() == 0:
                print("Bot win!")
            elif income_bot.get_income() == 0:
                print("You win!")   

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
