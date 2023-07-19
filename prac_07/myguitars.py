"""
CP1404 Prac 07 - More Guitars!
Estimated Time: 30 minutes
Actual time 50 minutes
"""
from prac_06.guitar import Guitar


def main():
    """Guitars - keep track of guitars and sort them."""
    guitars = []
    load_file(guitars)
    for guitar in guitars:
        print(guitar)
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        price = float(input("Price: "))
        guitars.append(Guitar(name, year, price))
        name = input("Name: ")
    save_file(guitars)


def load_file(guitars):
    """Load a file."""
    in_file = open("guitars.csv", 'r')
    for line in in_file:
        parts = line.strip().split(",")
        price = float(parts[2])
        guitar = Guitar(parts[0], parts[1], price)
        guitars.append(guitar)
    in_file.close()


def save_file(guitars):
    """Save a file."""
    out_file = open("guitars.csv", 'w')
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
