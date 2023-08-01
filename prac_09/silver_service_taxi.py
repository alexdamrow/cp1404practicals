"""
CP1404
SilverServiceTaxi
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of Taxi class, that includes fanciness and flagfall."""

    def __init__(self, name, fuel, fanciness):
        """Initialises a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Taxi, but with a flag fall"""
        return f"{super().__str__()}"

    def get_fare(self):
        """Return price from trip."""
        return self.price_per_km * self.start_fare()

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent class Taxi."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
