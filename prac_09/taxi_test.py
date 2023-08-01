from taxi import Taxi


def main():
    """Test the class Taxi."""
    my_taxi = Taxi("Prius 1", 100, 1.23)
    my_taxi.drive(40)
    print(f"{my_taxi}, {my_taxi.get_fare()}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"{my_taxi}, {my_taxi.get_fare()}")


main()
