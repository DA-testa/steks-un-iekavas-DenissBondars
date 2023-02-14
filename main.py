# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, position + 1))
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if (len(opening_brackets_stack) == 0) or not(are_matching(opening_brackets_stack[-1].char, next)):
                print (i+1)
                return i+1
            opening_brackets_stack.pop()
            pass
    if (len(opening_brackets_stack) == 0):
        print("Success")
    else:
        print(opening_brackets_stack[-1].position)
    pass


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    
    
if __name__ == "__main__":
    main()
