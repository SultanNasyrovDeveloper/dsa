"""
Reverse given string.
"""


def reverse_string(string: str) -> str:
    stack = []
    for char in string:
        stack.append(char)

    reversed_as_list = []
    while stack:
        reversed_as_list.append(stack.pop())
    return ''.join(reversed_as_list)


assert reverse_string('abc') == 'cba'
assert reverse_string('Python') == 'nohtyP'
