#main
from income import Income
from Croupier import croupier

try:
    new_croupier = croupier.Croupier("Ivan")
    new_croupier.add_card((1,2))
    print(new_croupier.get_amount())

except Exception as e:
    print(e)
