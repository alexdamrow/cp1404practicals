"""
CP1404
SilverServiceTaxi
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of Taxi class, that includes fanciness and flagfall."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialises a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Taxi, but with a flag fall"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return price from trip."""
        return self.flagfall + super().get_fare()


