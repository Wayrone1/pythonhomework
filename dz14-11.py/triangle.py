from math import sqrt 
class NotValidFigure(Exception):
    pass

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not self.is_valid():
            raise NotValidFigure

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimeter() / 2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

    def is_valid(self):
        sides = [self.a, self.b, self.c]
        if all([isinstance(side,(int, float)) for side in sides]): 
            if all ([side >= 0 for side in sides]):
                return all([side > 0 for side in sides])



triangle = Triangle(6, 12, 13)
print("Площадь треугольника:", round(triangle.square(),2))








