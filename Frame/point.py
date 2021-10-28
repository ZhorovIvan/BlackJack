
class Point:

    def __init__(self, sum_point):
        if str(sum_point).isnumeric() and sum_point >= 0 and sum_point < 5:
            self.point = sum_point
        else:
            raise Exception("You write incorrect sum point. Try again")


    def get_point(self):
        return self.point


    def set_point(self, value):
        if str(value).isnumeric():
            self.point = value
        else:
            raise Exception("You try to set not numeric")
