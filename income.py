
class Income:

    def __init__(self, income):
        if income.isnumeric() and income > 0:
            self.income = income
        else:
            raise Exception("You write incorrect the income. Try again")


    def get_income(self):
        return self.income

    def set_income(self, value):
        self.income += value
