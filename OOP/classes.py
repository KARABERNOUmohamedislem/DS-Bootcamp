
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def getArea(self):
        return self.length * self.width

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Vehicle:
    pass

class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)
