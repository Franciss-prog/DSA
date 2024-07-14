
number = int(input("Enter Number: "))

if number > 0: 
    print("Higher than zero")

    if number % 2 == 0:
        print("The number you entered is Even")
    else: 
        print("The number you entered is Odd")

else: 
    print("You put a negative number")