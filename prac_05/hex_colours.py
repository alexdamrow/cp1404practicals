HEXIDECIMAL_TO_COLOUR = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Alizarin Crimson": "#e32636",
                         "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "Apricot": "#fbceb1",
                         "Aqua": "#00ffff", "Army Green": "#4b5320", "Arylide Yellow": "#e9d66b"}
colour = input("Choose a colour: ").title()
while colour != "":
    try:
        print(f"{colour} is {HEXIDECIMAL_TO_COLOUR[colour]}")
    except KeyError:
        print("Invalid colour")
    colour = input("Choose a colour: ").title()
