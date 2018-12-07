import letters as ltr
import name as nm


def letters_to_numbers(your_name):
    name_array = nm.name_to_array(your_name)
    nbr = []
    for c in name_array:
        nbr.append(ltr.letter_to_number(c))

    return nbr


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


name = 'Flavio'
numbers = letters_to_numbers(name)

print(letters_to_numbers(name))

print(sum_list(numbers))
