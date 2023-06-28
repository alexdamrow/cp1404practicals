"""
Emails
Estimated: 35 minutes

"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        right_name = input(f"Is your name {name}? (Y/n) ")
        if right_name.upper() != "Y" and right_name != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")



def extract_name_from_email(email):
    username = email.split("@")[0]
    parts = username.split(".")
    name = " ".join(parts).title()
    return name



main()
