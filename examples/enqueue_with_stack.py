from typing import Any


class MyQueue:
    def __init__(self) -> None:
        self.stack1: list = []
        self.stack2: list = []

    def enqueue(self, value):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if len(self.stack1) == 0:
            return None
        return self.stack1.pop()

    def peek(self):
        return self.stack1[-1]


def main() -> None:
    queue: MyQueue = MyQueue()
    queue.enqueue(2)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(3)

    print(queue.peek())


if __name__ == "__main__":
    main()
