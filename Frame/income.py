
class Income:

    def __init__(self, income):
        if str(income).isnumeric() and income > 0 and income < 50:
            self.income = income
        else:
            raise Exception("You write incorrect the income. Try again")


    def get_income(self):
        return self.income


    def set_income(self, value):
        if str(value).isnumeric():
            self.income += value
        else:
            raise Exception("You try to set not numeric")


