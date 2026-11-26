# TextCrypt Program

import colorama # Making the program more colourful and easier to read

encryption_dictionary = {
    "a":"∆","b":"Ω","c":"π","d":"√","e":"©","f":"ß","g":"£","h":"¥","i":"§","j":"•",
    "k":"★","l":"☆","m":"☀","n":"☁","o":"☂","p":"☃","q":"♫","r":"♪","s":"☯","t":"☸",
    "u":"✈","v":"✉","w":"☘","x":"☕","y":"⚡","z":"☢",
    "A":"✿","B":"❀","C":"❁","D":"❂","E":"❃","F":"❄","G":"❅","H":"❆","I":"❇","J":"❈",
    "K":"❉","L":"❊","M":"❋","N":"◆","O":"◇","P":"○","Q":"●","R":"◐","S":"◑","T":"◒",
    "U":"◓","V":"◔","W":"◕","X":"◖","Y":"◗","Z":"◘",
    "0":"♠","1":"♣","2":"♥","3":"♦","4":"✦","5":"✧","6":"✩","7":"✪","8":"✫","9":"✬",
    " ":"~",".":"…",",":"¶","!":"⑀","?":"¿"
}

decryption_dictionary = {value: key for key, value in encryption_dictionary.items()}    # Reversing the encryption dictionary without having to rewrite the whole list


def textcrypt_menu():

    print(colorama.Fore.YELLOW + "*** - Please note: This program can only decrypt messages that were encrypted using 'TextCrypt.' "
    "\nTrying to decrypt messages from any other program will not give the correct result. - ***")

    print(colorama.Fore.GREEN + "\nO P T I O N S :")

    print(colorama.Fore.MAGENTA + '''
    1. Encrypt a Message
    2. Decrypt a Message
    3. Quit
    ''')


def encryption():

    print(colorama.Fore.RED + "\nPlease enter the message to encrypt: \n")
    encryption_message = input("" + colorama.Style.RESET_ALL)

    encrypted_message = ''.join(encryption_dictionary.get(c, c) for c in encryption_message)
    print(colorama.Fore.GREEN + f"\nEncrypted Message: {encrypted_message}\n")


def decryption():

    print(colorama.Fore.RED + "\nPlease enter the message to decrypt: \n")
    decryption_message = input("" + colorama.Style.RESET_ALL)

    decrypted_message = ''.join(decryption_dictionary.get(c, c) for c in decryption_message)
    print(colorama.Fore.BLUE + f"\nDecrypted Message: {decrypted_message}\n")


def play_textcrypt():

    print(colorama.Fore.RED + "\n---------- 👾 Welcome to my TextCrypt Program! 👾 ----------\n")

    while True:

        textcrypt_menu()

        choice = input(colorama.Fore.CYAN + "Please select one of the options above: " + colorama.Style.RESET_ALL).strip().lower()

        if choice in ["1", "encrypt", "encryption", "one"]:
            encryption()

        elif choice in ["2", "decrypt", "decryption", "two"]:
            decryption()

        elif choice in ["3", "quit", "q"]:
            print(colorama.Fore.YELLOW + "\nReturning to the ArcadeX menu...\n" + colorama.Style.RESET_ALL)
            return

        else:
            print(colorama.Fore.RED + "\nInvalid Option!\n" + colorama.Style.RESET_ALL)


if __name__ == "__main__":
    play_textcrypt()

