import random

# importing random library

print("====== Welcome to the Number Guessing Game! ======")
# Welcoming the player to the game
name = input("\nEnter your name: ")
# Prompting the player for name
answer_solution = random.randint(1, 20)
# Set random integer number between 1 and 10 to be selected to a variable answer_solution
attempts = 1
# creating a variable for attempts increments

while True:
    # Creating a while loop with conditional statements
    try:
        guessed_number = int(input(f"Hello {name.title()}, Choose a Number: "))
    # Prompting user to choose a number

    except ValueError:
        print("Invalid entry, Please try again.")
        attempts += 1
        continue
    if guessed_number == answer_solution:
        # Creating a condition for when the guessed number matches the random guessed number
        print(f"{name.title()}, You Guessed Right!")
        print(f"{name.title()}, It took you {attempts} attempts before guessing before Guessing Right!")
        # Showing player how many attempts if took to guess correct
        print(f"{answer_solution} was the Random Number Selected.")
        # Showing the random number that was chosen
        attempts += 1
        # Indicating attempts will increment by values of 1 each time an attempt is made
        print(f"{name.title()}, Thank you for playing The Number Guessing Game!")
        # Printing statement indicating the game has concluded and thanking the player for playing
        play_again = input(f"{name.title()}, Would you like to play again? (Y/N): ")
        if play_again == "Y":
            answer_solution = random.randrange(2, 20, 2)
            print(f"Beat your High Score: {attempts}")
            continue
            # Asking player if they want to play again
        elif play_again == "N":
            break
            # Ending game when players selects they no longer wish to play
        else:
            break
            # Stopping the loop after correct number is guessed
    elif guessed_number >= 21:
        # Condition if guessed number is out of range of the random number chosen
        print(f"{name.title()}, This number is out of Range!\tPlease Try Again!")
        attempts += 1
        continue
        # Loop continues until player guesses the correct number
    elif guessed_number < answer_solution:
        # Condition if guessed number is less than the random number chosen
        print(f"{name.title()}, It's Higher!")
        attempts += 1
        continue
        # Loop continues until player guesses the correct number
    elif guessed_number > answer_solution:
        # Condition if guessed number is greater than the random number chosen
        print(f"{name.title()}, It's Lower!")
        attempts += 1
        continue
        # Loop continues until player guesses the correct number


