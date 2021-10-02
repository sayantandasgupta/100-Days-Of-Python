# For calculating BMI, we need to take the height and weight from user input and calculate weight / height^2

# in this problem, we are going to determine based on certain metrics whether a person is underweight, overweight or normal

# Take the height and weight from the user

height = float(input("Enter the height in m: "))
weight = float(input("Enter the weight in kg: "))

# Calculate BMI

bmi = round(weight / (height**2), 2)

if bmi < 18.5:
    print("You are underwight")
elif bmi>=18.5 and bmi<25 :
    print("You are of normal weight")
elif bmi>=25 and bmi<30:
    print("You are overweight")
elif bmi>=30 and bmi<35:
    print("You are obese")
else:
    print("You are clinically obese")
