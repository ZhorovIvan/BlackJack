#main
from income import Income

try:
    f = Income("-1")
except Exception as e:
    print(e)
