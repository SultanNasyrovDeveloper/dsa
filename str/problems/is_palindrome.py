

def check_if_palindrome(string: str) -> bool:
    middle = len(string) // 2
    last_index = len(string) - 1
    for index in range(middle):
        if string[index] != string[last_index - index]:
            return False
    return True


assert check_if_palindrome('') is True
assert check_if_palindrome('aa') is True
assert check_if_palindrome('abccba') is True
assert check_if_palindrome('asdjhjkswbdfkhj') is False
assert check_if_palindrome('abcfcba') is True
assert check_if_palindrome('Abba') is True
