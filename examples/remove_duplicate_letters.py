def remove_duplicates(letters: str) -> str:
    stack: list[str] = []
    for i in letters:
        if i not in stack:
            stack.append(i)
    stack.sort()
    return "".join(stack)


def main() -> None:
    print(remove_duplicates("bcabc"))
    print(remove_duplicates("cbacdcbc"))


if __name__ == "__main__":
    main()
