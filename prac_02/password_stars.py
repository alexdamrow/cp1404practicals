NUMBER_OF_VARIABLES = 10
def main():
    """Display a password as stars."""
    password = get_valid_input("Enter password: ", NUMBER_OF_VARIABLES)
    print(convert_password(password))



def get_valid_input(prompt, boundary):
    """Makes sure an input is valid."""
    input_string = input(prompt)
    while len(input_string) < boundary:
        print("Invalid input")
        input_string = input(prompt)
    return input_string


def convert_password(password):
    """Convert a password to stars."""
    password_as_stars = len(password) * '*'
    return password_as_stars

main()