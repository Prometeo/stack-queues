class Stack:
    def __init__(self) -> None:
        self.my_list: list = []

    def push(self, value: int) -> None:
        self.my_list.append(value)

    def pop(self) -> int | None:
        if self.is_empty():
            return None
        return self.my_list.pop()

    def is_empty(self) -> bool:
        return len(self.my_list) == 0

    def peek(self) -> int | None:
        if self.is_empty():
            return None
        return self.my_list[-1]

    def print_stack(self):
        for i in range(len(self.my_list) - 1, -1, -1):
            print(self.my_list[i])


def sort_stack(stack: Stack) -> None:
    new_stack: Stack = Stack()

    while not stack.is_empty():
        temp = stack.pop()

        while not new_stack.is_empty() and new_stack.peek() > temp:
            stack.push(new_stack.pop())
        new_stack.push(temp)

    while not new_stack.is_empty():
        stack.push(new_stack.pop())


def main() -> None:
    list = [1, 6, 3, 4, 5, 2, 7]
    stack: Stack = Stack()
    for i in list:
        stack.push(i)
    sort_stack(stack)
    stack.print_stack()


if __name__ == "__main__":
    main()
