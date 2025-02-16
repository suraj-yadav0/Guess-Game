import random

# Read words from file
with open('sowpods.txt', 'r') as f:
    words = f.read().splitlines()

# Step 1: Select random word
target = random.choice(words).lower()  # Use choice instead of choices

# Step 2: Create initial display
user_guess = list("-" * len(target))  # Convert to list to make it mutable

print("Welcome to HangMan !!")
print("".join(user_guess))  # Join list to display as string
print("Try Guessing this word.")

# Step 3: Game loop
while '-' in user_guess:
    guess = input("Guess your letter: ").lower()

    if guess in target:
        print("Guessed Correctly!")
        # Update all occurrences of the guessed letter
        for i in range(len(target)):
            if target[i] == guess:
                user_guess[i] = guess
        print("".join(user_guess))  # Show current state
    else:
        print("Incorrect Guess.")

print(f"Congratulations! The word was {target}")