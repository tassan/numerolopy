import re
import unidecode


# split the given name on whitespaces
def name_to_array(person_name):
    return person_name.split(' ')


# turn the given name in an array of its letters
def letters_to_array(person_name):
    return [l for l in to_lower(person_name)]


def to_lowercase(word):
    return word.lower()


def replace_accents(word):
    return unidecode.unidecode(word)


def validate_name(person_name):
    name = person_name.replace('_', ' ')
    name = re.sub('[^ a-zA-Z]', '', to_lower(name))
    return name


me = 'Flavio Tassan dos Santos'
name_to_array(me)