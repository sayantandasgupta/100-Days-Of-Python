'''
Exercise 1 for Day 4 of 100 Days of Python

We are building a coin toss simulator for this exercise.

What we shall be learning:-

1. How to use the Random module to generate random integers

For this exercise, we are assigning the following numbers for Heads or Tails

1 - Heads
0 - Tails
'''

# We have to import the random module for generating random integers
import random

'''
The toss() function calls the random.randint() function and stores the generated number in a variable num

Depending on whether num contains 1 or 0, we assign the output variable to be Heads or Tails

The output is then printed.
'''


def toss():
    # Use the random.randint(a,b) function to generate a random number in the closed range [a,b]

    num = random.randint(0, 1)

    # This is one way of writing if else statements in one line
    output = 'Heads' if num == 1 else 'Tails'

    '''
    An alternate method would be the following

    if num == 1:
        output = 'Heads'
    else:
        output = 'Tails'
    '''

    print(f"The output is {output}")


if __name__ == '__main__':
    continueToss = 'yes'

    while continueToss == 'yes':
        toss()
        continueToss = input(
            "Toss Again? Type \'yes\' to continue or \'no\' to exit: ").lower()

    print("Thank you for playing this game! See you soon!")
