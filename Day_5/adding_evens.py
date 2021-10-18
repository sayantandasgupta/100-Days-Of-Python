'''
Exercise 3 for Day 5 of 100 Days of Python

For this exercise, we are going to find the sum of all the even numbers from 1 to 100, including 100

So, we need to find and print the result of 

2 + 4 + 6 + ... + 100
'''

'''
We can easily carry this out using a for loop and the range() generator. Let us define a function to carry out this functionality
'''

'''
find_even_number_sum does not take any parameters

It runs a for loop between 1 to 100 and adds all the even numbers present in that range.
We can use the range() generator with a step of 2 to get all the even numbers.

So the function first initialises a total as 0

Then as we access all the even numbers using the for loop, we add them one by one to the total
'''


def find_even_number_sum():

    totalSum = 0

    # From the working of a range function, we know that 2 is starting value, 102 is ending value and the second 2 is the step value
    for evenNo in range(2, 102, 2):
        # Quick Question: Why have we used 102 as ending value instead of 100? Think about it

        totalSum += evenNo

    print(
        f"Total Sum of the even numbers between 1 and 100, including 100 is {totalSum}")


if __name__ == '__main__':
    find_even_number_sum()
