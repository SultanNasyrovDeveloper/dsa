

def test_insert_into_min_heap(minheap):
    minheap.push(-2)
    previous_length = len(minheap.data)
    assert minheap.data[0] == -1
    assert len(minheap.data) == previous_length + 1
