# You can determine whether a number is odd or even using the modulo ( % ) operator

# An even number is perfectly divisible by 2 and odd numbers are not

# Therefore, if we divide an even number by 2 then the remainder should be 0 and for odd numbers the remainder will not be 0

# We shall find that out using if else statements quite easily

# first take an integer n from the user

n = int(input("Enter a number: "))

if n%2 == 0:
    print("Number is even")

else:
    print("Number is odd")
