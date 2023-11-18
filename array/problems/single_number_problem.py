"""
Given an array of integers where each number except one appear twice.
Find number that appears only once.

[1, 4, 5, 4, 3, 3, 1]
[1, 1, 3, 3, 4, 4, 5]

Solutions:
- brute force(using nested loop)
for each element iterate from the start of array to find if it has duplicates
Time Complexity: O(n^2)

- using sorting
Sort array iterate over

- using dict counter
iterate over array and store number of appearance in the dict

- using xor
"""