import math


class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        a, b = self.coor1
        x, y = self.coor2
        dquared = (x-a)**2 + (y-b)**2
        print(dquared)
        return math.sqrt(dquared)
