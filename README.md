# Guess the Number Game

A fun and interactive number guessing game built with Python. Test your luck and intuition by guessing a secret number between 1 and 100!

## Overview

This is a classic number guessing game with a twist—you can choose your difficulty level, which determines how many attempts you get to find the secret number. The game provides helpful hints ("Too High" or "Too Low") after each guess.

## Features

- **Three Difficulty Levels:**
  -  **Easy**: 10 attempts
  -  **Medium**: 7 attempts
  -  **Hard**: 5 attempts

- **Input Validation**: Ensures guesses are valid numbers between 1 and 100
- **Error Handling**: Gracefully handles invalid inputs
- **Helpful Feedback**: Tells you if your guess is too high or too low
- **Attempt Tracking**: Shows remaining guesses after each attempt
- **Win/Lose Conditions**: Reveals the secret number if you lose

##  How to Play

1. **Run the game:**
   ```bash
   python guess-number.py
   ```

2. **Choose a difficulty level** (1, 2, or 3)

3. **Start guessing!** Enter numbers between 1 and 100

4. **Use the hints** ("Too High" or "Too Low") to narrow down your range

5. **Win** by guessing the secret number before running out of attempts

##  Example Gameplay

```
Welcome to Guess the Number!
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
```

##  Requirements

- Python 3.x
- No external libraries required (uses only Python's built-in `random` module)

##  How It Works

| Step | Description |
|------|-------------|
| 1 | Player selects difficulty level (Easy/Medium/Hard) |
| 2 | Game generates random number between 1-100 |
| 3 | Player enters guesses and receives feedback |
| 4 | Game continues until player wins or runs out of attempts |
| 5 | Game reveals the secret number if player loses |

##  Technical Details

- **Language**: Python 3
- **Module Used**: `random.randint()` for generating random numbers
- **Input Handling**: Try-except blocks for error handling
- **Loop Structure**: Nested while loops for difficulty selection and main game loop

##  Learning Concepts

This project demonstrates:
- Loops (`while` loops)
- Conditional statements (`if`, `elif`, `else`)
- Exception handling (`try`, `except`)
- User input and validation
- String formatting (f-strings)
- Variable tracking and state management

##  License

This project is free to use and modify for educational purposes.

---

**Enjoy the game and test your guessing skills!** 
