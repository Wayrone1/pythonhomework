from math import sqrt 
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimeter() / 2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

triangle = Triangle(5, 12, 13)
print("Площадь треугольника:", triangle.square())