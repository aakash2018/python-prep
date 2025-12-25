def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False


print(is_palindrome("pop"))
print(is_palindrome("aakash"))
print(is_palindrome("121"))
