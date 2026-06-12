import random

# 1. Set the secret number
secret_number = random.randint(1, 20)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 20.")

# Bonus: Create counter for attempts
attempts = 0

# 2. Set up the loop
while True:
    # Get the player's guess
    guess = int(input("Guess a number between 1 and 20: "))
    
    # Increase attempt count
    attempts += 1
    
    # 3. Check the guess
    if guess > secret_number:
        print("Too high! Try again.")
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Congratulations! You guessed the correct number!")
        print(f"It took you {attempts} attempts.")
        break  # Exit the loop