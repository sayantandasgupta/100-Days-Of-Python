'''
Exercise 1 for Day 5 of 100 Days of Python

In this exercise, we are going to find out the average height from a list of given heights

This exercise is intended to make the user learn more about for loops in python
'''


def average_height(heights):
    '''
    One method is to use sum() and len() functions to find the average height from heights list

    we need to simply write

    return round( sum(heights)/len(heights) , 2)
    The round function is used to round of the result to a given number of decimal places, in this case 2
    '''

    '''
    An alternative method would be to find the sum of all the elements using a for loop and then dividing it by the length of the heights list
    '''

    height_sum = 0

    for height in heights:
        height_sum += height

    return round(height_sum / len(heights), 2)


if __name__ == '__main__':
    heights = [int(height) for height in input(
        "Enter the heights(in cm) of all the students in comma separated values: ").split(', ')]

    average = average_height(heights)

    print(f"Average height of all the students = {average} cm")
