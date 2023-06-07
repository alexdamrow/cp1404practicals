import random

def main():
    """Print result given a score"""
    score = float(input("Enter score: "))
    print(determine_result(score))

    random_score = random.randint(0, 100)
    print(determine_result(random_score))




def determine_result(score):
    """Determine result based off score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    else:
        return "Excellent"

main()