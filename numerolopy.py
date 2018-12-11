from letters import letters as ltr
from names import name as nm


def letters_to_numbers(person_name):
    numbers_list = []
    validated_name = nm.validate_name(person_name)

    name_array = nm.name_to_array(validated_name)

    if len(name_array) > 1:
        for name in name_array:
            for l in nm.letters_to_array(name):
                numbers_list.append(ltr.letter_to_number(l))
    else:
        for l in nm.letters_to_array(name_array):
            numbers_list.append(ltr.letter_to_number(l))
    return numbers_list


def number_len(number):
    return len(str(abs(number)))


def sum_digits(digits):
    digit_list = []
    if number_len(digits) >= 2:
        for digit in str(digits):
            digit_list.append(digit)
        return sum(digit_list)
    else:
        return sum(digits)


def sum_list(numbers_list):
    result = sum(numbers_list)
    return sum_digits(result)


me = 'Flávio'

print(letters_to_numbers(me))
