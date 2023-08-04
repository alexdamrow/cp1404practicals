"""
Band class for CP1404
Esimated: 30 minutes
Actual: 1 hr 20 minutes
"""

class Band:
    """Band class."""
    def __init__(self, band):
        """Construct a Band with a band name and an empty members list."""
        self.band = band
        self.members = []

    def __str__(self):
        """Return a string represent of a Band instance."""
        return f"{self.band} ({','.join([str(member) for member in self.members])})"

    def add(self,  member):
        """Add member to band."""
        self.members.append(member)

    def play(self):
        """Can the member play his instrument."""
        return '\n'.join([member.play() for member in self.members if member.play() is not None])


