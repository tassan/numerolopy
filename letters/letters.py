alphabet_dictionary = {
    1: ['a', 'j', 's'],
    2: ['b', 'k', 't'],
    3: ['c', 'l', 'u'],
    4: ['d', 'm', 'v'],
    5: ['e', 'n', 'w'],
    6: ['f', 'o', 'x'],
    7: ['g', 'p', 'y'],
    8: ['h', 'q', 'z'],
    9: ['i', 'r']
}

letters_dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 1,
    'k': 2,
    'l': 3,
    'm': 4,
    'n': 5,
    'o': 6,
    'p': 7,
    'q': 8,
    'r': 9,
    's': 1,
    't': 2,
    'u': 3,
    'v': 4,
    'w': 5,
    'x': 6,
    'y': 7,
    'z': 8
}


def letter_to_number(letter):
    return letters_dictionary[letter]
