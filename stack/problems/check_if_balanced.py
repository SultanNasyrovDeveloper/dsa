"""
Given a string containing open and closed brackets.
Check if string is balanced eg all open brackets are closed.

Solutions:
    
"""


def check_if_balanced(string: str) -> bool:
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for char in string:
        if char in brackets:
            stack.append(char)
        else:
            last_open = stack.pop()
            if char != brackets[last_open]:
                return False
    return not stack


assert check_if_balanced('') is True
assert check_if_balanced('()') is True
assert check_if_balanced('([]}') is False
assert check_if_balanced('((') is False
assert check_if_balanced('[()]{}{[()()]()}') is True
