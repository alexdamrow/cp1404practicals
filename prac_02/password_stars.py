NUMBER_OF_VARIABLES = 10
def main():
    password = get_valid_input("Enter password: ", NUMBER_OF_VARIABLES)
    print(len(password) * '*')



def get_valid_input(prompt, boundary):
    input_string = input(prompt)
    while len(input_string) < boundary:
        print("Invalid input")
        input_string = input(prompt)
    return input_string

main()