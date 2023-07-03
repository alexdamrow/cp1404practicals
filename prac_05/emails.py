"""
Emails
Estimated: 35 minutes
Actual: 45 minutes
"""
"""
Dictionary with email and name as key and value
"""


def main():
    """Create and print dictionary based around emails."""
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
    """Extract name from email."""
    username = email.split("@")[0]
    parts = username.split(".")
    name = " ".join(parts).title()
    return name



main()
