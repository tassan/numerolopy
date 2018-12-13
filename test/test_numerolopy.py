import numerolopy as nlp

name = 'Flavio'
number = 29
number_list = [6, 3, 1, 4, 9, 6]


assert nlp.letters_to_numbers(name) == number_list

assert nlp.number_len(number) == 2

assert nlp.sum_digits(number) == 2

assert nlp.find_numerology(name) == 2

