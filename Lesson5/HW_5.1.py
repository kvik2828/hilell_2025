import string
import keyword


user_input = str(input("Please enter name variable: "))

first_simb = user_input[0]
simbol_two = user_input.count('_')
first_simb_no_number = first_simb.isalpha() or bool(simbol_two)
input_no_punctuation = user_input not in string.punctuation or bool(simbol_two)
input_no_keyword = user_input not in keyword.kwlist

if simbol_two == 1:
    INP = True
elif  simbol_two == 0:
    INP = True
else:
    INP = False

if simbol_two == 1:
    low_registr = True
else:
    low_registr = (user_input.islower())


print(first_simb_no_number and (user_input.islower() or bool(simbol_two)) and INP and input_no_keyword and input_no_punctuation)

