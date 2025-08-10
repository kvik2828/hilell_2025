import string


lst = []

for char in string.ascii_letters:
    lst.append(char)

user_input = str(input("Please enter 2 letters l-l: "))
let_1 = user_input[0]
let_2 = user_input[-1]

index_of_let_1 = lst.index(let_1)
index_of_let_2 = lst.index(let_2)

result = lst[index_of_let_1 : index_of_let_2+1]
result_str = "".join(result)

print(result_str)

