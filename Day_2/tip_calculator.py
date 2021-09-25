'''
This is Day 2 of 100 Days of Python
Today, we are going to build a tip calculator
The knowledge that we need are basic school mathematics and the usage of the different operators in Python

In python the different operators used are +, - , *, /, // , **, and the % operators.
Each has its own function, which we shall explore in this Tip Calculator Program

This Program is intended for the understanding of operators and mathematical operations in Python
This has no real life usage unless you are revising or learning how to make basic mathematical operations in Python.

Difficulty Level: Easy
Knowledge To be Gained: Introduction to basic Mathematical operators and operations in Python
'''

#First of all let us print a welcome message for the user

message = "Welcome to Tip Calculator"

print(message)

# The next thing to do is to take the total bill amount as input

totalBillAmount = float(input("What is the total bill? $ "))

# After taking input the total bill amount, take input the number of persons who shall split the bill among themselves, and the percentage of the bill which is to be given as tip

numberOfPersons = int(input("Enter the total number of persons: "))
tipPercentage = float(input("Enter the percentage of bill to be paid as tip: "))

# After taking all the inputs, now comes the calculation part. First thing we need to calculate is the tip amount

tip = (totalBillAmount * tipPercentage) / 100 # For percentage, multiply the billAmount by Percentage and divide by 100


# Add the tip to the totalBillAmount to find the totalPayableAmount

totalPayableAmount = totalBillAmount + tip

# Finally divide the totalPayableAmount by the total number of persons to find how much amount each person has to pay, round it off to 2 decimal places using round() method, and print the result using an fstring

amountToPay = totalPayableAmount / numberOfPersons

print(f"Each person has to pay $ {round(amountToPay,2)}")
