import letters as ltr
import name as nm


def letters_to_numbers(your_name):
    name_array = nm.name_to_array(your_name)
    nmbs = []
    for c in name_array:
        nmbs.append(ltr.letter_to_number(c))

    return nmbs


def number_len(number):
    return len(str(abs(number)))


def sum_list(numbers_list):
    result = sum(numbers_list)

    if number_len(result) > 2:
        pass

# sum digits


name = 'Flavio'
numbers = letters_to_numbers(name)

print(letters_to_numbers(name))

print(sum_list(numbers))
