from letters import letters as ltr
from names import name as nm


def letters_to_numbers(person_name):
    validated_name = nm.validate_name(person_name)
    letters_array = [l for l in validated_name]
    return [ltr.letter_to_number(n) for n in letters_array]


def number_len(number):
    return len(str(abs(number)))


def sum_digits(digits):
    digit_list = [int(n) for n in str(digits)]
    result = sum(digit_list)
    if number_len(result) == 2:
        result = sum_digits(result)
    return result


def find_numerology(person_name):
    pass


