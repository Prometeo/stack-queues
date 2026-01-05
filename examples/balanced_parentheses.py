class Stack:
    def __init__(self) -> None:
        self.my_list: list = []

    def push(self, value: str) -> None:
        self.my_list.append(value)

    def pop(self) -> str | None:
        if self.is_empty():
            return None
        else:
            return self.my_list.pop()

    def size(self) -> int:
        return len(self.my_list)

    def is_empty(self) -> bool:
        return len(self.my_list) == 0


def is_balanced_parentheses(parentheses) -> bool:
    stack = Stack()
    for p in parentheses:
        if p == "(":
            stack.push(p)
        elif p == ")":
            print(stack.my_list)
            if stack.is_empty() or stack.pop() != "(":
                return False

    return stack.is_empty()


def main() -> None:
    paren: str = "(()"
    return is_balanced_parentheses(paren)


if __name__ == "__main__":
    print(main())
