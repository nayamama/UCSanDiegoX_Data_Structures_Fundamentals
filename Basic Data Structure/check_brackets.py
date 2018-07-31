# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    position_list = [Bracket(char, i + 1) for (i, char) in enumerate(text)]
    opening_brackets_stack = []

    for item in position_list:
        if item.char in "([{":
            opening_brackets_stack.append(item)
        if item.char in ")]}":
            if len(opening_brackets_stack) != 0 and are_matching(opening_brackets_stack[-1].char, item.char):
                opening_brackets_stack.pop()
            else:
                return item.position

    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return opening_brackets_stack[0].position


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
