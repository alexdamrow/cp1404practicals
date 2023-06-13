"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   ValueError will occur when a value other than an whole integer e.g. string
   or decimal is entered.

2. When will a ZeroDivisionError occur?
   This will occur when the denominator is 0, as that is impossible.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   To avoid a ZeroDivisionError error checking using a while loop could be
   used to ensure the denominator is not 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Invalid denominator")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")