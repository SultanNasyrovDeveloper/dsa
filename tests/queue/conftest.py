import pytest
from collections.abc import Callable
from random import randint

from q.llist_queue import Queue, QueueNode


@pytest.fixture
def empty_queue() -> Queue:
    return Queue()


@pytest.fixture
def queue_factory() -> Callable[[int], Queue]:

    def inner(size: int) -> Queue:
        assert size > 0
        queue = Queue()
        root = QueueNode(randint(1, 100))
        queue.root = root
        if size > 1:
            current = root
            for _ in range(size - 1):  # because we already created root
                current.next = QueueNode(randint(1, 100))
                current = current.next
            queue.tail = current
        queue.size = size
        return queue
    return inner

