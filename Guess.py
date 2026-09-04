import random


def user_value(attempt):
    print(f"\nAttempt {attempt} of 3")

    while True:
        value = int(input("Enter a number between 1 and 10: "))

        if 1 <= value <= 10:
            return value
        else:
            print("Please enter a number within the range.")


def computer_value():
    return random.randint(1, 10)


def compare_values(user, computer):

    for attempt in range(1, 4):

        if user == computer:
            print("Congratulations! You guessed the correct number.")
            return True

        else:
            print("Incorrect guess.")

        if attempt < 3:
            remaining = 3 - attempt
            print(f"You have {remaining} attempts left.")

            user = user_value(attempt + 1)

    print("Sorry, you've used all your attempts.")
    print("The correct number was:", computer)

    return False


print("\tGUESSING GAME")
print("------------------------------")
print("You have 3 attempts to guess the correct number.")


while True:

    continue_game = input("\nDo you want to play the game? (yes/no): ").lower()

    if continue_game == "no":
        print("Exiting the game. Goodbye!")
        break

    elif continue_game == "yes":

        # Start a new game
        user = user_value(1)
        computer = computer_value()

        compare_values(user, computer)

    else:
        print("Please enter yes or no.")
