import random

MIN_BOUNDARY = 1
MAX_BOUNDARY = 45
AMOUNT_OF_NUMBERS = 6


def main():
    """Quick picks"""
    quick_picks = get_valid_integer("How many quick picks: ", 0)
    for i in range(quick_picks):
        numbers = []
        for j in range(AMOUNT_OF_NUMBERS):
            pick = random.randint(MIN_BOUNDARY, MAX_BOUNDARY)
            while pick in numbers:
                pick = random.randint(MIN_BOUNDARY, MAX_BOUNDARY)
            numbers.append(pick)
        numbers.sort()
        print(" ".join(f"{pick:2}" for pick in numbers))


def get_valid_integer(prompt, minimum):
    number = int(input(prompt))
    while number < minimum:
        print("Invalid input")
        number = int(input(prompt))
    return number


main()
