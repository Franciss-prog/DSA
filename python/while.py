import random

def guessing_game(secret_number):
    while True:
        try:
            guess_number = int(input("Enter your Guessed Number (1-10): "))
            if 1 <= guess_number <= 10:
                break
            else:
                print("Input Error: Number must be between 1 and 10")
        except ValueError:
            print("Input Error: Please enter a valid integer")

    # Compare the guess with the secret number
    if guess_number == secret_number:
        print(f"Congratulations! You guessed the secret number: {secret_number}!")
    else:
        print(f"Sorry, the secret number was {secret_number}. Try again.")

while True:
    print("Welcome to Guessing Game")
    start = input("Do you want to play? Y/n: ")

    # Validate start input
    if start.strip().lower() == "n":
        print("Thank you for your cooperation....")
        break    
    elif start.strip().lower() != "y":
        print("Input Error: must be Y or N")
        continue

    while True:
        # Generate a random number between 1 and 10 for each new game
        secret_number = random.randint(1, 10)

        # Call the guessing game function with the secret number
        guessing_game(secret_number)

        play_again = input("Do you want to play again? Y/n: ")
        if play_again.strip().lower() == "n":
            break
    
    if play_again.strip().lower() == "n":
        print("Thank you for playing!")
        break
