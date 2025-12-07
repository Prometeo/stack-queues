import pytest
from main import Stack, Queue


# ~> Fixtures
@pytest.fixture
def base_stack() -> Stack:
    return Stack(1)


@pytest.fixture
def base_queue() -> Queue:
    return Queue(1)


def test_push_item(base_stack: Stack):
    base_stack.push(2)
    assert base_stack.top.value == 2
    assert base_stack.top.next.value == 1
    assert base_stack.height == 2


def test_pop_item(base_stack: Stack):
    base_stack.push(2)
    base_stack.push(3)
    height = base_stack.height
    print(height)
    result = base_stack.pop()
    assert result.value == 3
    assert base_stack.height == (height - 1)
    assert base_stack.top.value == 2


def test_enqueue(base_queue: Queue):
    base_queue.enqueue(2)
    base_queue.enqueue(3)
    assert base_queue.length == 3
    assert base_queue.first.value == 1
    assert base_queue.last.value == 3


def test_dequeue(base_queue: Queue):
    base_queue.enqueue(2)
    result = base_queue.dequeue()
    assert result.value == 1
    assert base_queue.length == 1
    assert base_queue.first.value == 2
