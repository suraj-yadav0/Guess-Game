str = input("Enter a String:")


def is_palindrome(str):
    return str == str[::-1]

print(is_palindrome(str))

