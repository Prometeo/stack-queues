# Reverse a string


class Stack:
    def __init__(self) -> None:
        self.my_list: list = []

    def push(self, value: str):
        self.my_list.append(value)

    def pop(self) -> str | None:
        return self.my_list.pop()

    def reverse_string(self) -> str:
        result: str = ""
        for i in range(len(self.my_list)):
            result = result + self.my_list.pop()
        return result


def main() -> None:
    my_string: str = "Hello World"
    stack = Stack()
    for i in my_string:
        stack.push(i)

    print(stack.reverse_string())


if __name__ == "__main__":
    main()
