'''
Exercise 2 for Day 5 of 100 Days of Python

In this exercise, we are going to find out the highest score from a given list of scores of a certain number of students

We are going to discuss 2 methods of finding the maximum
'''


def find_maximum_score(scores):
    ''' METHOD 1
    Using the inbuilt max() function, which takes an iterable as its parameter and returns the maximum value in the iterable
    x = max(scores)
    return x
    '''

    '''METHOD 2
    Declare a global max value. Compare with each and every value inside the list and update the max value accordingly
    Use a for loop for your comparisons
    '''

    maxVal = scores[0]  # declare the first value as the maxVal

    # Now using a for loop compare the maxVal with each and every item and then update if maxVal is less than one particular item
    for i in range(1, len(scores)):
        if maxVal < scores[i]:
            maxVal = scores[i]

    return maxVal


if __name__ == "__main__":
    scores = [int(score) for score in input(
        "Enter the scores of the students in comma separated form: ").split(', ')]

    maximumScore = find_maximum_score(scores)

    print(f"The highest score is {maximumScore}")
