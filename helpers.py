import string


def alphabet_position(letter):
    alphabet = {}

    for index, l in enumerate(range(97, 123)):
        alphabet[chr(l)] = index

    return alphabet[letter.lower()]


def rotate_character(char, rot):
    is_upper = char.isupper()
    is_alpha = char.isalpha()

    if is_alpha:
        position = alphabet_position(char)
        final_position = (position + rot) % 26

        if is_upper:
            alphabet = string.ascii_uppercase
        else:
            alphabet = string.ascii_lowercase

        return alphabet[final_position]

    else:
        return char