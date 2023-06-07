MENU = """(G)et 
(P)rint
(S)how
(Q)uit"""
def main():
    """Interactive menu."""
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_input("Enter score: ", 0, 100)
        elif choice == "P":

        elif choice == "S":

        else:
            print("Invalid ")
        choice = input(">>>").upper()
    print("Farewell")

def get_valid_input(prompt, min_number, max_number):
    """Get a valid input."""
    score = int(input(prompt))
    while score < min_number or score > max_number:
        print("Invalid input")
        score = int(input(prompt))
    return score


