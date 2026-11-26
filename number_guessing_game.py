# Number Guessing Game

import random

def ask_yes_no(prompt):

    while True:

        answer = input(prompt).strip().lower()

        if answer in ["yes", "y"]:
            return True

        elif answer in ["no", "n"]:
            return False

        print("\nPlease enter a valid answer!")
        

def guessing_round():    # One round of the guessing game

    lives = 5
    number = random.randint(1, 100)

    while True:

        print("\nThe computer has chosen a number between 1 and 100. You have 5 lives. For every wrong guess you lose 1 life.")

        try:
            guess = int(input("\nPlease enter your guess (1 - 100): "))

        except ValueError:
            print("\nPlease enter a whole number!")
            continue

        if guess < 1 or guess > 100:
            print("\nYour guess must be between 1 and 100!")
            continue

        if guess == number:
            print(f"\nWell done! You have guessed the number! You still have {lives} lives.")
            return

        lives -= 1
        print(f"\nIncorrect! You just lost a life. You have {lives} lives left.")

        if lives <= 0:
            print(f"\nYou lost! The correct answer was {number}.")
            return

        hint = input("\nWould you like me to give you a hint? (yes/no): ").strip().lower()

        if hint in ["yes", "y"]:

            level = input("\nPlease select the hint level you would like to receive. Level 1 (1): Free (simple hint). Level 2 (2): One life will be deducted from your total, but you will receive a good hint. ").strip()

            if level == "1":

                if abs(guess - number) <= 5:
                    print("\nHint Level 1: You're VERY close!")

                elif abs(guess - number) <= 15:
                    print("\nHint Level 1: You're close!")

                else:
                    print("\nHint Level 1: You're far off!")

            elif level == "2":

                if lives <= 1:
                    print("\nYou don't have enough lives for a Level 2 hint!")

                else:
                    lives -= 1

                    if 1 <= number <= 25:
                        print("\nHint Level 2: The number is between 1 - 25.")

                    elif 26 <= number <= 50:
                        print("\nHint Level 2: The number is between 26 - 50.")

                    elif 51 <= number <= 75:
                        print("\nHint Level 2: The number is between 51 - 75.")

                    elif 76 <= number <= 100:
                        print("\nHint Level 2: The number is between 76 - 100.")

            else:
                print("\nInvalid hint level. No hint given.")

        elif hint in ["no", "n"]:
            print("\nI like that confidence! No hints will be given. Good Luck!")


def play_guessing_game():

    print('''

--------------------------------------------
        N U M B E R   G U E S S I N G
--------------------------------------------

''')

    while True:

        guessing_round()

        if not ask_yes_no("\nWould you like to play again? (yes/no): "):
            print("\nThanks for playing!")
            return


if __name__ == "__main__":
    play_guessing_game()

