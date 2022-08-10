#!/usr/bin/python3

def ispalindrome(x: int) -> bool:
    """return true if an int ispalindrom without converting int to str"""
    if x < 0:
        return False
    div = 1
    while x >= 10 * div:
        div *= 10
    while x:
        if x // div != x % 10:
            return False
        x = (x % div) // 10
        div = div / 100
    return True
    


b = 121
print(ispalindrome(b))

c = -121
print(ispalindrome(c))

d = 1001
print(ispalindrome(d))

e = 0
print(ispalindrome(e))