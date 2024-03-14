def is_palindrome(text):
    return text == text[::-1]
text = input()
print(is_palindrome(text))