class Node:
    def __init__(self, x) -> None:
        self.value = x
        self.next = None


def is_palindrome(my_list: Node) -> bool:
    stack = []
    tmp = my_list
    while tmp:
        stack.append(tmp.value)
        tmp = tmp.next

    for i in range(len(stack) // 2):
        if stack[i] != stack.pop():
            return False

    return True


def main():
    head: Node = Node(1)
    head.next: Node = Node(2)
    head.next.next: Node = Node(2)
    head.next.next.next: Node = Node(1)

    print(is_palindrome(head))


if __name__ == "__main__":
    main()
