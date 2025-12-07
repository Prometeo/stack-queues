class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.next: Node | None = None


class Stack:
    # Filo: First in last out
    def __init__(self, value):
        new_node: Node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value: int):
        new_node: Node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self) -> None | int:
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next


class Queue:
    # Fifo: first in first out
    def __init__(self, value):
        new_node = Node(value)
        self.first: Node = new_node
        self.last: Node = new_node
        self.length = 1

    def enqueue(self, value):
        new_node: Node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self) -> Node | None:
        if self.first is None:
            return None
        item = self.first
        if self.length == 1:
            self.first = None
            self.laste = None
        if self.first.next:
            self.first = self.first.next
        item.next = None
        self.length -= 1
        return item

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
