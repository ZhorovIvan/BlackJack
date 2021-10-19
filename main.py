#main
from Frame import income as inc
from Croupier import croupier


def main():
    try:
        i = inc.Income(30)
        print(i.get_income())
        
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
