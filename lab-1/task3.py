a = input('Введите палиндром на проверку ');

def is_palindrome(string):
    return string == ''.join(reversed(string))

print(is_palindrome(a))
