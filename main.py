#main
from Frame import income as inc
from Croupier import croupier
from Frame import console

startTest = "Welcome to my new game!"
incorrectInput = "You write incorrect word. Try again!"
choiseInputText = "You gotta choose next step (Stop or take)\n"
stopWord = "stop"
takeWord = "take"


def main():
    try:
        print(startTest)
        while(True):
            choiceHumon = str(input(choiseInputText))
            if choiceHumon.lower() == stopWord:
                break
            elif choiceHumon.lower() == stopWord:
                break
            else:
                print(incorrectInput)
                continue
         
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
