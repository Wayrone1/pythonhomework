import math 

class Circle:
    def __init__(self, radius):
        self.radius = radius 

    def square(self):
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        return 2 * math.pi * self.radius
 
radius = int(input("Введите радиус круга: "))
obj = Circle(radius)
print("Площадь круга:", round(obj.square(), 2))
print("Длина окружности:", round(obj.perimeter(), 2))