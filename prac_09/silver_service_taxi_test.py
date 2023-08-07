"""
CP1404
Test for class SilverServiceTaxi
"""
from silver_service_taxi import SilverServiceTaxi


def main():
    """Test the class SilverServiceTaxi"""
    my_taxi = SilverServiceTaxi("Hummer", 200, 2)
    print(my_taxi)
    my_taxi.drive(18)
    print(my_taxi.get_fare())


main()
