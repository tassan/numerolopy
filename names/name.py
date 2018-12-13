import re
import unidecode


def name_to_array(person_name):
    return person_name.split(' ')
# split the given name on whitespaces


def letters_to_array(person_name):
    lowercase_name = to_lowercase(person_name)
    return [l for l in lowercase_name]
# turn the given name in an array of its letters


def to_lowercase(word):
    return word.lower()
# turn any word to lowercase


def replace_accents(word):
    return unidecode.unidecode(word)
# replace any letter with accents to the same one without it


def validate_name(person_name):
    name = replace_accents(person_name)
    name = name.replace('_', ' ')
    name = re.sub('[^ a-zA-Z]', '', to_lowercase(name))
    return name
# validate the given name
