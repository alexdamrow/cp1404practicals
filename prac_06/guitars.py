from prac_06.guitar import Guitar

guitars = []
print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = int(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print("")
    name = input("Name: ")
