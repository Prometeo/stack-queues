# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#    Open brackets must be closed by the same type of brackets.
#    Open brackets must be closed in the correct order.
#    Every close bracket has a corresponding open bracket of the same type.

open_paren: list = []


def is_balanced(my_str: str) -> bool:
    close_paren: dict[str, str] = {")": "(", "}": "{", "]": "["}
    for i in my_str:
        if i not in close_paren.keys():
            open_paren.append(i)
        else:
            if len(open_paren) == 0:
                return False
            if close_paren[i] != open_paren.pop():
                return False
    return True


def main() -> None:
    test1: str = "()"
    print(is_balanced(test1))
    test2 = "()[]{}"
    print(is_balanced(test2))
    test3 = "([)]"
    print(is_balanced(test3))
    test4 = "(]"
    print(is_balanced(test4))


if __name__ == "__main__":
    main()
