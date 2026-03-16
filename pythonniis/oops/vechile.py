from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speed(self):
        pass


class Car(Vehicle):
    def __init__(self, name, maxspeed):
        super().__init__(name)
        self.maxspeed = maxspeed

    def speed(self):
        return self.maxspeed


class Bike(Vehicle):
    def __init__(self, name, maxspeed):
        super().__init__(name)
        self.maxspeed = maxspeed

    def speed(self):
        return self.maxspeed


c1 = Car("BMW", 240)
print("Car speed:", c1.speed())

b1 = Bike("Yamaha", 180)
print("Bike speed:", b1.speed())
