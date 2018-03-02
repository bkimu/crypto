from helpers import rotate_character
from sys import argv, exit


def encrypt(text, rot):
    encrypted_text = ""
    for char in text:
        encrypted_text = encrypted_text + rotate_character(char, rot)

    return encrypted_text


def main():
    #rot = int(input("Rotate by:"))
    if len(argv) > 1 and argv[1].isdigit():
        text = input("Type a message:")
        print(encrypt(text, int(argv[1])))
    else:
        print("Please enter a valid integer as an argument")
        exit()


if __name__ == "__main__":
    main()