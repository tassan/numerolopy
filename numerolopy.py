from letters import letters as ltr
from names import name as nm


def letters_to_numbers(FullName):
    validated = nm.validate_name(FullName)
    validated = [validated.split(' ')]


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


me = 'Flávio Tassan dos Santos Filho'

print(letters_to_numbers(me))
