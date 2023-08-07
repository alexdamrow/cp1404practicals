"""
CP1404
Unreliable car test
"""
from unreliable_car import UnreliableCar


def main():
    """Test the class UnreliableCar."""
    my_car = UnreliableCar("Ford Falcon", 100, 50)
    my_car.drive(40)
    print(my_car)


main()
