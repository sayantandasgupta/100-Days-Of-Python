'''
This is the 5th problem on Day 3 based on if else and if statements
In this problem, we are going to build a love calculator which shall calculate compatibility between 2 people

if score < 10 or score > 90, we have to print Your score is this, you go together like coke and mentos
if score >=40 and score <= 50 we have to print Your score is this, you are alright together
else print your score is this
'''

'''
The following function calculates the love compatibility between 2 people

Don\'t have to take this value seriously ;-). It is meant to be a fun project and created for the general understanding of if-elif-else and basic for loops

This function takes 2 names as input. 

Then it counts the number of times the letters of the word TRUE occur in the 2 names. Let that be count_true
Secondly, it counts the number of times the letters of the word LOVE occur in the 2 names. Let that be count_love

Finally, the result is created by putting count_true in ten's place and count_love in unit's place

For example:-

name1 = Luis
name2 = Gerard

count_true = 4
count_love = 2

Result = 42
'''


def loveCalculator():
    name1 = input("Enter your name: ").lower()
    name2 = input("Enter your loved one\'s name: ").lower()

    count_true = 0
    count_love = 0

    for s in name1:
        if s in 'true':
            count_true += 1
        if s in 'love':
            count_love += 1
    for s in name2:
        if s in 'true':
            count_true += 1
        if s in 'love':
            count_love += 1

    score = (count_true*10) + count_love

    if score < 10 or score > 90:
        print(f"Your score is {score}, you go together like coke and mentos")
    elif score >= 40 and score <= 50:
        print(f"Your score is {score}, you are alright together")
    else:
        print(f"Your score is {score}")


if __name__ == "__main__":
    loveCalculator()
