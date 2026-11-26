# ArcadeX

from hangman import play_hangman
from number_guessing_game import play_guessing_game
from rock_paper_scissors import play_rps
from textcrypt import play_textcrypt


def main():

    print('''

############################################
#                                          #
#               A R C A D E X              #
#                                          #
############################################
''')

    print("         *** Welcome to ArcadeX! ***")

    while True:

        print("\nPlease choose a game from the options below:\n")
        print("1. Hangman")
        print("2. Number Guessing Game")
        print("3. Rock, Paper, Scissors")
        print("4. TextCrypt")
        print("5. Quit (Q / 5)")

        choice = input("\nPlease enter your choice (1 - 5): ").strip().lower()

        if choice in ["1", "hangman"]:
            play_hangman()

        elif choice in ["2", "guessing", "number guessing game"]:
            play_guessing_game()

        elif choice in ["3", "rps", "rock paper scissors"]:
            play_rps()

        elif choice in ["4", "textcrypt"]:
            play_textcrypt()

        elif choice in ["5", "q", "quit"]:
            print("\n*** Thanks for playing ArcadeX! ***\n")
            break

        else:
            print("\nInvalid Choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()

