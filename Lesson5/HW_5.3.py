import string

user_input = input(str("Please enter name: "))
user_input = user_input.title()
punct = str(string.punctuation)

punct_lst = list(punct)

chars_to_replace = punct_lst
for char in chars_to_replace:
    user_input = user_input.replace(char, ' ')

user_input_strip = "".join(user_input.split())

result = "#" + user_input_strip
print(result[:139])