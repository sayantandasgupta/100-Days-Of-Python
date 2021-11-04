'''
Final Project for Day 5 of 100 Days of Python Code

In this project, we are going to create a password generator by taking some information from the user.

We are going to take the desired length of the password and then generate a password of the same length with a combination of letters,
numbers and special characters.

We have to use the string and the random modules for creating this password generator.
'''

import random # for the randomly generating the password
import string # for getting access to all possible letters, numbers and special characters


def generate_password():
    # Step 1: Print the welcome message and take the desired length of the password as an input from the user

    print("Welcome to PyPassword Generator")

    n = int(input("Enter the desired length of your password: "))

    # Step 2: Create a string containing all letters, uppercase or lowercase, integers and special characters from where we shall pick random characters and put it into our password

    ALL_CHARACTERS = string.ascii_letters + string.digits + string.punctuation  # The sample string containing all the letters, numbers and special characters

    # Step 3: Randomly select characters from the ALL_CHARACTERS string and generate the password

    password = ''.join(random.choice(ALL_CHARACTERS) for i in range(n))

    print(f"Your generated password is {password}")


if __name__ == '__main__':
    # Call the generate password function

    generate_password()