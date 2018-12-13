from names import name

person_name = 'Flavio Tassan'
name_array = ['f', 'l', 'a', 'v', 'i', 'o']
fullname_array = ['Flavio', 'Tassan']
name_Uppercase = 'FLAVIO'


assert name.name_to_array(person_name) == fullname_array

assert name.to_lowercase(name_Uppercase) == 'flavio'

assert name.letters_to_array('flavio') == name_array
