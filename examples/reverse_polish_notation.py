operators: str = "+-*/"


def eval_rpn(tokens: list[str]) -> int:
    stack = []

    for i in tokens:
        if i not in operators:
            stack.append(i)
        else:
            right = int(stack.pop())
            left = int(stack.pop())
            if i == "-":
                stack.append(left - right)
            elif i == "+":
                stack.append(left + right)
            elif i == "*":
                stack.append(left * right)
            elif i == "/":
                stack.append(left / right)
    return stack.pop()


def main():
    print(eval_rpn(["2", "1", "+", "3", "*"]))
    print(eval_rpn(["4", "13", "5", "/", "+"]))
    print(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))


if __name__ == "__main__":
    main()
