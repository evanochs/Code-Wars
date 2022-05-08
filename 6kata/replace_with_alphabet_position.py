#My Solution

import string
alph = string.ascii_lowercase
def alphabet_position(text):
    pass
    result=[]
    for char in text.lower():
        if char in alph:
            result.append(str(alph.find(char)+1))
    return(" ".join(result))




alphabet_position("The sunset sets at twelve o' clock.")

#CodeWars #1 Solution

def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())