
# IS211 Assignment 7 - Pig Dice Game

## Overview
This project is a Python version of the Pig Dice Game created for IS211 Week 7. It demonstrates Object-Oriented Programming (OOP) by using classes to manage players, dice rolls, and gameplay.

## How to Play
The game has two human players. The goal is to be the first player to reach 100 points.

- Enter `r` to roll the die.
- Rolling 2 through 6 adds points to the current turn.
- Rolling a 1 ends the turn, and the player loses the points accumulated during that turn.
- Enter `h` to hold and add the turn points to the overall score.
- The first player to reach 100 points wins.

## Object-Oriented Design
The program uses three classes:

- **Player:** Stores each player's name and score.
- **Die:** Generates random dice rolls from 1 through 6.
- **PigGame:** Manages player turns, scoring, and the winning condition.

## Running the Game
Run the following command in Terminal:

`python3 pig.py`

## Testing
The project includes five automated unit tests that check player scoring, dice rolls, turn rules, and game completion.

Run the tests using:

`python3 -m unittest test_pig.py`

The five unit tests passed successfully.

