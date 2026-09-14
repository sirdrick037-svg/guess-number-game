#  Guess the Number Game

A fun and interactive number guessing game built with Python. Test your luck and intuition by guessing a secret number between 1 and 100! Track your progress with the built-in leaderboard system.

## Overview

This is a classic number guessing game with a twist—you can choose your difficulty level, which determines how many attempts you get to find the secret number. The game provides helpful hints ("Too High" or "Too Low") after each guess, tracks your username, calculates your score, and displays a leaderboard showing all players' best scores.

## Features

- **Username System**: Enter your name to track your progress
- **Three Difficulty Levels:**
  -  **Easy**: 10 attempts
  -  **Medium**: 7 attempts
  -  **Hard**: 5 attempts

- **Scoring System**: Earn points based on difficulty level and number of attempts used
  - Harder difficulties earn more points
  - Fewer attempts = higher score
  
- **Leaderboard**: View top 10 players with their best scores, attempts, and difficulty level
- **Input Validation**: Ensures guesses are valid numbers between 1 and 100
- **Error Handling**: Gracefully handles invalid inputs
- **Helpful Feedback**: Tells you if your guess is too high or too low
- **Attempt Tracking**: Shows remaining guesses after each attempt
- **Score Persistence**: Scores are saved to a JSON file and persist between sessions
- **Win/Lose Conditions**: Reveals the secret number if you lose

##  How to Play

1. **Run the game:**
   ```bash
   python guess-number.py
   ```

2. **Main Menu** - Choose one of three options:
   - Play Game
   - View Leaderboard
   - Exit

3. **Enter your username** when prompted

4. **Choose a difficulty level** (1, 2, or 3)

5. **Start guessing!** Enter numbers between 1 and 100

6. **Use the hints** ("Too High" or "Too Low") to narrow down your range

7. **Win** by guessing the secret number before running out of attempts

8. **Check the Leaderboard** to see your rank and compare scores with other players

##  Example Gameplay

```
==================================================
GUESS THE NUMBER GAME 
==================================================
1. Play Game
2. View Leaderboard
3. Exit
Enter your choice (1, 2, or 3): 1

Enter your username: Alice

Welcome to Guess the Number!
Player: Alice
I'm thinking of a number between 1 and 100.

Choose a difficulty level:
1. Easy   - 10 tries
2. Medium - 7 tries
3. Hard   - 5 tries
Enter 1, 2, or 3: 2

You chose Medium difficulty.
You have 7 guesses. Good luck!

Enter your guess (1-100): 50
 Too Low!
Remaining guesses: 6

Enter your guess (1-100): 75
 Too High!
Remaining guesses: 5

Enter your guess (1-100): 62
 Correct! You guessed the number in 3 attempt(s)!

 Your Score: 900 points!
```

##  Leaderboard Example

```
==================================================
 LEADERBOARD - TOP 10 PLAYERS 
==================================================
 1. Alice                | Score:   900 | Attempts: 3 | Difficulty: Medium
 2. Bob                  | Score:   800 | Attempts: 2 | Difficulty: Easy
 3. Charlie              | Score:   750 | Attempts: 3 | Difficulty: Hard
==================================================
```

##  Requirements

- Python 3.x
- No external libraries required (uses only Python's built-in modules: `random`, `json`, `os`, `datetime`)

##  Scoring System

Points are calculated based on:
- **Difficulty Multiplier**: Harder difficulties earn more points
  - Easy: 1x multiplier
  - Medium: 2x multiplier
  - Hard: 3x multiplier
- **Attempt Bonus**: Fewer attempts = more points
  - Formula: `(max_attempts - attempts_used + 1) × 100 × difficulty_multiplier`
- **Best Score Tracking**: Only your best score per difficulty is saved

##  How It Works

| Step | Description |
|------|-------------|
| 1 | Player enters username |
| 2 | Main menu displays: Play, Leaderboard, Exit |
| 3 | Player selects difficulty level (Easy/Medium/Hard) |
| 4 | Game generates random number between 1-100 |
| 5 | Player enters guesses and receives feedback |
| 6 | Game continues until player wins or runs out of attempts |
| 7 | On winning, score is calculated and saved to `scores.json` |
| 8 | Player can view leaderboard showing top 10 players |

##  Technical Details

- **Language**: Python 3
- **Modules Used**: 
  - `random.randint()` - Generate random numbers
  - `json` - Store/retrieve scores from file
  - `os.path` - Check if scores file exists
  - `datetime` - Timestamp score entries
- **Data Storage**: Scores stored in `scores.json` (automatically created)
- **Input Handling**: Try-except blocks for error handling
- **Loop Structure**: Menu loop + game loop for continuous play
- **File Persistence**: Scores persist across game sessions

##  Learning Concepts

This project demonstrates:
- Loops (`while` loops, menu loop)
- Conditional statements (`if`, `elif`, `else`)
- Exception handling (`try`, `except`)
- User input and validation
- String formatting (f-strings)
- Variable tracking and state management
- **File I/O**: Reading and writing JSON files
- **Data Structures**: Dictionaries and JSON
- **Functions**: Modular code with reusable functions
- **Score Calculation**: Mathematical operations and logic
- **Sorting**: Sorting data for leaderboard display
- **Data Persistence**: Saving data between sessions

##  License

This project is free to use and modify for educational purposes.

---

**Enjoy the game and test your guessing skills!** 
