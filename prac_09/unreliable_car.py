"""
CP1404
UnreliableCar class
"""
from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of Car that includes reliability percentage."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like Car, but including the reliability."""
        return f"{super().__str__()}, reliability={self.reliability}%"

    def drive(self, distance):
        """Drive like parent Car, but only if random integer is less than reliability."""
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return super().drive(0)



