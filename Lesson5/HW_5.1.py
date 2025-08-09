import string
print(string.punctuation)
import keyword
print(keyword.kwlist)


user_input = str(input("Please enter name variable: "))
first_simb = user_input[0]
simbol_two = user_input.count('_')
input_no_punctuation = user_input.isalnum() or bool(simbol_two)

input_no_keyword = user_input not in keyword.kwlist

first_simb_no_number = first_simb.isalpha() or bool(simbol_two)

low_regist = (user_input.islower()) and bool(simbol_two)

if simbol_two == 0:
    INP = True
elif simbol_two == 1:
    INP = True
elif simbol_two >= 2:
    INP = False

print(first_simb_no_number and (user_input.islower() or bool(simbol_two)) and INP and not input_no_keyword and input_no_punctuation)

