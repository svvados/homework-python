import string
import random

def generate_password(length):
    if length < 8:
        print("The password must be at least 8 characters long.")
        return None

    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = random.sample(all_characters, length)

    if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
        return ''.join(password)
    else:
        return generate_password(length)


def password_generator():
    print("\nWelcome to the password generator!\n")
    while True:
        length_input = input("Enter password length (minimum 8 characters): ")
        try:
            length = int(length_input)
        except ValueError:
            print("\nError: You must enter a number.")
            continue

        generated_password = generate_password(length)
        if generated_password:
            print("\nGenerated password:", generated_password)
        repeat = input("\nDo you want to generate another password? (Y/N): ")
        if repeat.lower() != 'y':
            break


password_generator()
