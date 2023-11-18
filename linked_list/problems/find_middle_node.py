"""
Find middle node of linked list

Solutions:
one iteration with additional list O(n)/O(n)
- iterate over linked list and store its values in array
- get index of target element by floor/ceil division of target by two
- get element

two iterations O(n)/O(1)
- iterate over linked list ot find its length.
- count number of second element using floor or ciel division
- iterate second time until counter not equals to length of middle element

two pointers method: O(n)/O(1)
- init two pointers slow and fast
- start while loop till fast pointer reaches the end
- on each step set slow pointer to next and fast pointer to netx next.
- when fast pointer reaches the end slow pointer will point to middle

odd counter method: O(n)/O(1)
- init counter variable and middle variable initially equals to ten
- iterate over linked list and update counter on each step
- move middle element to middle next only on odd numbers
"""
from typing import Any

from linked_list.generator import generate_linked_list
from linked_list.list import LinkedList, Node


def get_middle(llist: LinkedList) -> Any:
    counter = 0
    middle = llist.head
    current = llist.head

    while current:
        if counter & 1:
            middle = middle.next
        current = current.next
        counter += 1
    return middle.value


llist1 = generate_linked_list(amount=5, start=1, sequential=True)
llist2 = generate_linked_list(amount=6, start=1, sequential=True)
assert get_middle(llist1) == 3
assert get_middle(llist2) == 4


