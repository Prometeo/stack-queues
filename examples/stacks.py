# push and pop stack


class Stack:
    def __init__(self) -> None:
        self.stack_list: list = []

    def push(self, value: int) -> None:
        self.stack_list.append(value)

    def pop(self) -> int | None:
        if len(self.stack_list) == 0:
            return None
        return self.stack_list.pop()
