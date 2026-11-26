# ArcadeX 🎮

A command line mini game centre written in Python. Choose a game from the menu and enjoy a relaxing, interactive gaming session. When a game ends, you return to the menu to pick another one.

## What it does

* **Multiple mini games** to choose from, all in one place
* **Replay option** so you can play again once a game is over
* **Difficulty levels** in some games to make things more challenging
* **Hint system** in some games to help you out when you are stuck
* **Score tracking** in Rock, Paper, Scissors
* **Input validation**, so unexpected entries such as letters instead of numbers don't crash the program

## The files

| File | Description |
|------|-------------|
| `ArcadeX.py` | The main menu. Run this file to start |
| `hangman.py` | Guess the hidden word one letter at a time before you run out of attempts, with three difficulty levels |
| `number_guessing_game.py` | Guess the secret number between 1 and 100 before you run out of lives, with two levels of hints |
| `rock_paper_scissors.py` | Play against the computer and keep track of the score |
| `textcrypt.py` | Encode your messages into symbols and decode them back again |

## How to use it

1. Make sure you have Python 3 installed.
2. Install the required library, which is used by TextCrypt:

```
pip install colorama
```

3. Keep all of the files in the same folder.
4. Run `ArcadeX.py`.
5. Enter the number of the game you want to play and follow the on screen prompts.

## Built with

* Python 3
* Colorama for the coloured text in TextCrypt
