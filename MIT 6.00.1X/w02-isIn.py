def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    hi = len(aStr)
    lo = 0

    if hi == 0 or (hi == 1 and aStr[0] != char):
        return False

    middleChar = aStr[int(len(aStr) // 2)]
    middleInt = int(len(aStr) // 2)

    if char == middleChar:
        return True
    elif char < middleChar:
        hi = middleInt
        aStr = aStr[lo:hi]
        return isIn(char, aStr)
    elif char > middleChar:
        lo = middleInt
        aStr = aStr[lo:hi]
        return isIn(char, aStr)
    else:
        return 'You Done Goofed'


print(isIn('a', ''))
# False
print(isIn('c', 'aefhjkllnqrryy'))
# False
print(isIn('h', 'abfhnopttvvwyz'))
# True