# python3
#221RBD463, Reds Ričards Polis
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def are_matching2(left, right):
    if (left + right) in ["()", "[]", "{}"]:
        return True # kad izveidojās atverošās/aizverošās iekavu pārītis
    else:
        return False # kad neizveidojās atverošās/aizverošās iekavu pārītis
    


def find_mismatch(text):
    print("tests2")
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                print (i)
            pass
            if len(opening_brackets_stack) != 0:
                if (are_matching2(opening_brackets_stack.pop(), next) == False):
                    print(i)
                pass
            pass
        pass



def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here

print ("tests")

#if __name__ == "__main__":
main()
pass