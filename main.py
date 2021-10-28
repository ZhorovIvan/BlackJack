#main
from Frame import console,point,game
import time
import configparser


config = configparser.ConfigParser()  
config.read("config.ini") 


def main():
    count_game = 0
    try:
        health = point.Point(3)
        print(config["Main"]["start_text"])
        game.preparation()
        while(True):
            count_game += 1
            result_game = game.round() 
            if result_game == "Win":
                print(config["Main"]["text_if_you_win_round"])
                health.set_point(health.get_point() + 1)
            elif result_game == "Lose":
                print(config["Main"]["text_if_you_lose_round"])
                health.set_point(health.get_point() - 1)
            elif result_game == "Draw":
                print(config["Main"]["text_if_draw_round"])
            
            if health.get_point() > 5:
                print(config["Main"]["test_win_game"])
                break
            elif health.get_point() == 0: 
                print(config["Main"]["text_lose_game"])  
                break
            time.sleep(4)   
            console.clear_desk()     
            print("Next round. You have: " + str(health.get_point()) + " health")
    except Exception as e:
        print(e.with_traceback())


if __name__ == "__main__":
    main()
