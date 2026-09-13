import random

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")

print("\nChoose a difficulty level:")
print("1. Easy   - 10 tries")
print("2. Medium - 7 tries")
print("3. Hard   - 5 tries")

while True:
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        max_attempts = 10
        level = "Easy"
        break
    elif choice == "2":
        max_attempts = 7
        level = "Medium"
        break
    elif choice == "3":
        max_attempts = 5
        level = "Hard"
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

secret_number = random.randint(1, 100)

print(f"\nYou chose {level} difficulty.")
print(f"You have {max_attempts} guesses. Good luck!")

attempts = 0

while attempts < max_attempts:
    try:
        guess = int(input("\nEnter your guess (1-100): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue

    attempts += 1
    remaining = max_attempts - attempts

    if guess == secret_number:
        print(f"\n Correct! You guessed the number in {attempts} attempt(s)!")
        break

    elif guess > secret_number:
        print("Too High!")

    else:
        print("Too Low!")

    if remaining > 0:
        print(f"Remaining guesses: {remaining}")
    else:
        print(f"\n Game Over! You ran out of guesses.")
        print(f"The number was {secret_number}.")