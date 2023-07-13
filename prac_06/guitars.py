from prac_06.guitar import Guitar

guitars = []
print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print("")
    name = input("Name: ")
print("These are my guitars: ")
for i, guitar in enumerate(guitars):
    vintage_string = guitar.is_vintage()
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")