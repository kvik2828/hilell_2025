def is_palindrome(text):

    sentence = ''
    for char in text:
        if char.isalnum():
            sentence = sentence + char.lower()

    reversed_sentence = ''.join(reversed(sentence))

    return sentence == reversed_sentence

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'

print("ОК")