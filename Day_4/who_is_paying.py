'''
This is exercise 2 for Day 4 of 100 Days of Python

In this exercise, we are going to take a list of names from the user and randomly return a name.

That person has to pay the bill for the entire group

This is a good exercise to learn more about how to generate random choices
'''

# We are again going to use the random module since we are trying to generate some random choices

import random

'''
The choose() function takes a list of names as its input parameter, and makes a random choice which shall be displayed by the function

We shall see 2 ways of generating a random choice from the given list of names.

One is the random.choice() method present in the random module which helps us to choose randomly from an iterable object

Secondly, we shall use random.randint() method for selecting a random name
'''


def choose(list_of_names):
    '''
    Method 1 - Using random.choice() method

    name = random.choice(list_of_names)
    print(name + " has to pay the entire bill.")
    '''

    '''Method 2 - Without using random.choice()'''

    random_idx = random.randint(0, len(list_of_names)-1)

    name = list_of_names[random_idx]

    print(name + " has to pay the entire bill")


if __name__ == '__main__':
    names = input("Enter all of the names separated by commas: ").split(', ')

    choose(names)
