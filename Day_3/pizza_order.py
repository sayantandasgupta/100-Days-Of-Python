'''
This is the 4th problem based on if else and multiple if statements in Python
In this problem we have to make an automated pizza taking program
The program shall take the order and specifications from the customer and print the total bill calculated

The rates are as follows:-

Small Pizza = $ 15
Medium Pizza = $ 16
Large Pizza = $ 25

Pepperoni for Small Pizza = + $2
Pepperoni for Medium or Large Pizza = + $3
Extra cheese for any size pizza = + $1
'''

'''
The calculateBill() function does the entire work that we have to calculate
It takes the size of the pizza as input and initialises the totalBill with the necessary prices
After that it asks whether the customer wants pepperoni and extra cheese wih the pizza
Depending on the answers, we shall add some amount of money to the totalBill or not
'''


def calculateBill():
    totalBill = 0

    pizzaSize = input(
        "What size pizza do you want? Please enter \'S\' for small, \'M\' for medium, and \'L\' for Large: ").lower()

    if(pizzaSize == 's'):
        totalBill = 15
        wants_pepperoni_for_small = input(
            "Do you want pepperoni with this? Please enter \'Y\' for yes and \'N\' for no: ").lower()
    elif(pizzaSize == 'm'):
        totalBill = 20
        wants_pepperoni_for_medium_or_large = input(
            "Do you want pepperoni with this? Please enter \'Y\' for yes and \'N\' for no: ").lower()
    else:
        totalBill = 25
        wants_pepperoni_for_medium_or_large = input(
            "Do you want pepperoni with this? Please enter \'Y\' for yes and \'N\' for no: ").lower()

    wants_extra_cheese = input(
        "Do you need extra cheese with this? Please enter \'Y\' for yes and \'N\' for no: ").lower()

    if(pizzaSize == 's' and wants_pepperoni_for_small == 'y'):
        totalBill += 2
    if((pizzaSize == 'm' or pizzaSize == 'l') and wants_pepperoni_for_medium_or_large == 'y'):
        totalBill += 3
    if(wants_extra_cheese == 'y'):
        totalBill += 1

    print(f"Your total bill is ${totalBill}")


if __name__ == "__main__":
    calculateBill()
