# functions
def add (x, y):
    return x + y

def minus (x,y):
    return x - y

def divide (x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def multiply (x,y):
    return x * y


def calculate (num1, num2, choice):
    if choice == "1":
        return add(num1, num2)
    if choice == "2":
        return minus(num1, num2)
    if choice == "3":
        return multiply(num1, num2)
    if choice == "4":
        return divide(num1, num2)

# main function
def main():
    print("Welcome to Calculator...")
    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        # choice input
        choice = int(input("Choose a operation (1/2/3/4/5):"))

        if choice == "5":
            # exit the calcu
            print("Exiting Calculator..")
            break

        # input validation
        if choice not in ("1", "2", "3", "4"):
            # print the error
            print("Input Error: must be 1,2,3,4...")
            continue

        # get int to user
        num1 = float()
        
main()

            



        



