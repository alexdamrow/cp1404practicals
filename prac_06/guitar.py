"""CP1404 Practical - Guitars!
Estimated time: 40 minutes
Actual time: 50 minutes """

YEAR = 2023
VINTAGE_THRESHOLD = 50


class Guitar:
    """Represent a Guitar object"""
    def __init__(self, name="", year=0, cost=0):
        """
        Initialise a Guitar instance.
        name: string, name of the guitar
        year: integer, year the guitar was first produced
        cost: float, price of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of data in a Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of a guitar."""
        age = YEAR - self.year
        return age

    def is_vintage(self):
        """Determine if a guitar is vintage based off a threshold."""
        return self.get_age() >= VINTAGE_THRESHOLD

