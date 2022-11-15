from math import pi
class NotValidFigure(Exception):
    pass

class Circle:
    def __init__ (self, radius):      
        self.radius = radius
        if not self.is_valid():
            raise NotValidFigure

    def length(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * (self.radius ** 2)

    def is_valid(self):
        if isinstance(self.radius,(int,float)):
            return self.radius > 0 


circle = Circle(3)
print("Площадь круга:", round (circle.area(),2))  
print("Длина окружности:", round (circle.length(),2))
