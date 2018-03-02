from helpers import alphabet_position, rotate_character
from sys import argv, exit


def encrypt(text, key):
    startingIndex = 0
    encrypted = []

    for letter in text:
        if letter.isalpha() == True:
            rotation = alphabet_position(key[startingIndex % len(key)])
            encrypted.append(rotate_character(letter, rotation))
            startingIndex += 1
        else:
            encrypted.append(letter)
    return ''.join(encrypted)


def main():
    print("This is what the user typed on the command line:", argv)
    if len(argv) > 1 and argv[1].isalpha():
        text = input("Type a message:")
        #key = input("Encryption key:")
        print(encrypt(text, argv[1]))
    else:
        print(
            '-keyword : The string to be used as a "key" to encrypt your message.'
            +
            'Should only contain alphabetic characters-- no numbers or special characters.'
        )
        exit()


if __name__ == "__main__":
    main()