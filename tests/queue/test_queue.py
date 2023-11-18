

def test_enqueue_empty_queue(empty_queue):
    queue = empty_queue
    enqueue_value = 25
    queue.enqueue(enqueue_value)
    assert queue.root == queue.tail
    assert queue.root.value == enqueue_value
    assert queue.size == 1


def test_enqueue(queue_factory):
    queue = queue_factory(20)
    enqueue_value = 25
    previous_size = queue.size
    queue.enqueue(25)
    assert queue.size == previous_size + 1
    assert queue.root.value == enqueue_value


def test_dequeue(queue_factory):
    queue = queue_factory(20)
    previous_size = queue.size
    previous_root = queue.root
    queue.dequeue()
    assert queue.size == previous_size - 1
    assert queue.root != previous_root


def test_dequeue_from_single_value_queue(queue_factory):
    queue = queue_factory(1)
    queue.dequeue()
    assert queue.size == 0
    assert queue.root is None
    assert queue.tail is None

