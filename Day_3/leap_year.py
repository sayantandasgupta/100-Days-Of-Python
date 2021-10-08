def checkLeap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

year = int(input("Enter the year: "))

if checkLeap(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")