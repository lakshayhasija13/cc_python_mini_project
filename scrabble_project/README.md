# Scrabble Project

A Python script that calculates Scrabble word scores and tracks player totals.

## Description

This project builds a letter-to-points dictionary by zipping the alphabet with standard Scrabble tile values, then defines a `score_word()` function that sums the point values for each letter in a word. It scores a sample word ("BROWNIE"), and then computes the total points for each player in a dictionary of players and their word lists.

## Concepts Used

- Dictionaries (`dict`, `zip`)
- Functions
- Loops (`for` loop)
- String iteration
- `print()` statements

## Sample Output

```
14
{'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}
...
{'player1': 29, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31}
```

## How to Run

```bash
python code.py
```
