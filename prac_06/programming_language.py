"""CP1404 Practical - programming language class
Estimated time: 30 minutes
Actual time: 35 minutes """


class ProgrammingLanguage:
    """Represent information about a programming language."""
    def __init__(self, name="", typing="", reflection="", year=0):
        """
        Initialise a Programming language instance.
        name: string, the name of the programming language
        typing: string, is the language dynamic or static
        reflection: bool, the language is reflective
        year: integer, year that language was first used
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of data in a ProgrammingLanguage object."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Returns true or false if language is dynamic."""
        return self.typing == "Dynamic"