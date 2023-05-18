import random  # Import random module to generate the winning number

print("WELCOME TO NUMBER GUESS GAME")

# Generate a random winning number between 1 and 100
winning_number = random.randint(1, 100)

guess = 1  # Initialize the guess counter

# Use a while loop to keep the game going until the player wins
while True:
    number = input("Enter a number between 1 and 100: ")
    num = int(number)  # Convert user input to integer

    # Check if the user's guess is correct
    if num == winning_number:
        print(f"YOU WIN!!! and you guessed the number in {guess} attempts.")
        break  # End the game if the user wins

    # If the guess is incorrect, give a hint to the user and ask them to guess again
    if num < winning_number:
        print("Too low.")
    else:
        print("Too high.")
    guess += 1  # Increase the guess counter by 1
guess=guess+1