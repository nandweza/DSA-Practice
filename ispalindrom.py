def ispalindrome(name: str) -> bool:
    name2 = name[::-1]

    if name == name2:
        return True
    return False


a = 'ana'
a = ispalindrome(a)

print(a)

b = 'ane'
b = ispalindrome(b)

print(b)
