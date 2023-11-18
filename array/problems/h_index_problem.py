"""
observations:
- h index is definitely smaller that array length
- if some element in array has value more than len of array this does not mean anything to us
because if those numbers are equals to array length this is enough information for us.

[0, 1, 2, 5, 6, 6, 6]

Solutions
- brute force(nested loops)

- using sort. O(n log n) O(1)
sort the array
star iterating over array
for each element check if array length - current element position(i + 1) is smaller than 0
it means that previous element is h index

using sort more clever
sort array
create current h index value that equals to 1
start iterating from the end of the list and check
if current value is more that current h index than hindex ++
else return h index --

using counting sort
perform count sort
it is suitable here because of the second observation
"""