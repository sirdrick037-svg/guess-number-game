import random
import json
import os
from datetime import datetime

SCORES_FILE = "scores.json"

def load_scores():
    """Load scores from JSON file."""
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, "r") as f:
            return json.load(f)
    return {}

def save_scores(scores):
    """Save scores to JSON file."""
    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f, indent=2)

def display_leaderboard(scores):
    """Display top 10 players by score."""
    if not scores:
        print("\n No scores yet! Be the first to play!")
        return
    
    print("\n" + "=" * 50)
    print("LEADERBOARD - TOP 10 PLAYERS")
    print("=" * 50)
    
    sorted_scores = sorted(
        [(name, score_data["score"], score_data["attempts"], score_data["difficulty"]) 
         for name, score_data in scores.items()],
        key=lambda x: (-x[1], x[2])
    )[:10]
    
    for rank, (name, score, attempts, difficulty) in enumerate(sorted_scores, 1):
        print(f"{rank:2d}. {name:20s} | Score: {score:5d} | Attempts: {attempts} | Difficulty: {difficulty}")
    print("=" * 50)

def calculate_score(attempts, max_attempts, level):
    """Calculate score based on difficulty and attempts."""
    difficulty_multiplier = {"Easy": 1, "Medium": 2, "Hard": 3}
    base_score = (max_attempts - attempts + 1) * 100
    return base_score * difficulty_multiplier[level]

def play_game(username):
    """Main game function."""
    print("\nWelcome to Guess the Number!")
    print(f"Player: {username}")
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
    won = False

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
            print(f"\nCorrect! You guessed the number in {attempts} attempt(s)!")
            won = True
            break

        elif guess > secret_number:
            print("Too High!")

        else:
            print("Too Low!")

        if remaining > 0:
            print(f"Remaining guesses: {remaining}")
        else:
            print(f"\nGame Over! You ran out of guesses.")
            print(f"The number was {secret_number}.")

    if won:
        score = calculate_score(attempts, max_attempts, level)
        scores = load_scores()
        
        if username not in scores or scores[username]["score"] < score:
            scores[username] = {
                "score": score,
                "attempts": attempts,
                "difficulty": level,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        
        save_scores(scores)
        print(f"\nYour Score: {score} points!")

def main():
    """Main menu."""
    while True:
        print("\n" + "=" * 50)
        print("GUESS THE NUMBER GAME")
        print("=" * 50)
        print("1. Play Game")
        print("2. View Leaderboard")
        print("3. Exit")
        
        menu_choice = input("Enter your choice (1, 2, or 3): ")
        
        if menu_choice == "1":
            username = input("\nEnter your username: ").strip()
            if not username:
                print("Username cannot be empty!")
                continue
            play_game(username)
        
        elif menu_choice == "2":
            scores = load_scores()
            display_leaderboard(scores)
        
        elif menu_choice == "3":
            print("\nThanks for playing! Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()