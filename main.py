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
    opening_brackets_stack = []
    #for i, next in enumerate(text):
    for i in range(0, len(text)): 
          #if next in "([{":
          if text[i] in "([{":
               # Process opening bracket, write your code here
               # opening_brackets_stack.append(Bracket(next,i))
               opening_brackets_stack.append(text[i])
        
          if text[i] in ")]}":
               # Process closing bracket, write your code here
               if len(opening_brackets_stack) == 0: # ja steks ar iekavaam ir tuks
                      return i+1           # steks ir tukšs
               else:  
                      if (are_matching2(opening_brackets_stack.pop(),text[i]) == False):
                          return i+1       # kluda, jo nesakrit iekavas
    if len(opening_brackets_stack) == 0:   # vai nepalika vēl stekā atverošās iekavas
        return ("Success")                 # visas iekavas iztērētas 
    else:
        return i+1                         # kluda, jo nesakrit iekavas  


def main():
    x = input("Ievadiet pārbaudāmo simbolu virkni:")
    print()
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

main()
