from prac_06.guitar import Guitar


def main():
    guitars = []
    in_file = open("guitars.csv", 'r')
    for line in in_file:
        parts = line.strip().split(",")
        price = float(parts[2])
        guitar = Guitar(parts[0], parts[1], price)
        guitars.append(guitar)
    in_file.close()

    for guitar in guitars:
        print(guitar)

    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()
