#main
from logging import raiseExceptions
from Frame import console,income
from Cards import cards
import time


#create config file
start_test = "Welcome to my new game!\nPlease, write income down"
incorrect_input = "You write incorrect value. Try again!"
choise_input_text = "You gotta choose next step (stop or take)\n"
stop_word = "stop"
take_word = "take"
income_human = income.Income(0)
income_bot = income.Income(0)
is_classic_game = True
desk_cards = cards.DeskOfCards()



def preparation():
    try:
        #search bug in the income class
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
        

#remove in another lolation
def game():
    humon_stop_step = False
    game = True
    try:
        new_human_desk = console.Desk()
        new_bot_desk = console.Desk()  
        desk_cards.create_cards(is_classic_game)
        while(game):
            if not humon_stop_step:
                #take another method
                choice_humon = str(input(choise_input_text))
                if choice_humon.lower() == take_word:
                    console.clear_desk()
                    new_human_desk.add_card(desk_cards.get_card())
                    print(new_human_desk.get_all_cards("Your"))
                elif choice_humon.lower() == stop_word:
                    is_lose = new_human_desk.has_too_many_cards()
                    humon_stop_step = True
                else:
                    print(incorrect_input)
                    continue
            else:
                time.sleep(1)
                console.clear_desk()
                new_bot_desk.add_card(desk_cards.get_card())
                print(new_bot_desk.get_all_cards("Bot"))
                game = new_bot_desk.is_enouth()
                is_lose = new_bot_desk.has_too_many_cards()
        print("game over!!!")
        #If u win return true
        return True    
    except Exception as e:
        print(e)


def main():
    count_game = 0
    try:
        print(start_test)
        preparation()
        while(True):
            count_game += 1  
            if game():
                #make another method for this
                income_human.set_income(income_human.get_income() + 1)
                income_bot.set_income(income_bot.get_income() - 1)
                print("You win game - " + str(count_game) +\
                     "\nYour income - " + str(income_human.get_income()))
            else:
                income_human.set_income(income_human.get_income() - 1)
                income_bot.set_income(income_bot.get_income + 1)
                print("You lose game - " + str(count_game) +\
                     "\nYour income - " + str(income_human.get_income()))  

            if income_human.get_income() == 0:
                print("Bot win!")
            elif income_bot.get_income() == 0:
                print("You win!")  
            time.sleep(4)   
            console.clear_desk()     
            print("Next round")
    except Exception as e:
        print(e.with_traceback())


if __name__ == "__main__":
    main()
