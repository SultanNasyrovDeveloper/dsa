"""
Detect anagram problem.
String is anagram if all characters of first str are in the second str.

Solutions:
- Brute force
Iterate over first str and for every character check if it in second str.
Time Complexity: O(n^2)
Space Complexity: O(1)

- Sorting
Two strings are anagrams if both sorted str are equal
Time Complexity: O(n log n)
Space Complexity: O(n)

- Cached counters
Iterate over both str and save characters appearance counter inside hash map.
If they are equal str are anagrams
Time complexity: O(n)/O(nk)
Space Complexity: O(n)/O(nk)

- Cached counter slightly memory usage improved
Iterate over first str and save its character usage.
Iterate over second str and lower (-=) its character usage.
On each step os second str iteration if some character not in counter or new counter value after
subtract is less than 0 you can definitely say str are not anagram.
check if all counter values are zero.

Time complexity: O(n)/O(nk)
Space Complexity: O(n)/O(n)
"""


def check_if_anagram(first: str, second: str) -> bool:
    first_counter = {}
    second_counter = {}

    for character in first:
        first_counter[character] = first_counter.get(character, 0) + 1

    for character in second:
        second_counter[character] = second_counter.get(character, 0) + 1

    return first_counter == second_counter


assert check_if_anagram('test', 'stet')