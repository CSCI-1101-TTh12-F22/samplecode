# palindrome check for for/each syntax
# returns true if backwards == forwards
def palindrome1(s1):
    s2 = ""
    for c in s1:
        s2 = c  + s2
    print(s2, s1)
    if s1 == s2:
        return True
    else:
        return False

# palindrome check for for/range syntax
# returns true if backwards == forwards
def palindrome2(sf):
    sb = ""
    for i in range(len(sf)-1, -1, -1):
        sb = sb + sf[i]
    print(sf, sb)
    if sf == sb:
        return True
    else:
        return False

# palindrome check with for/each that
# returns immediatley when a non-matching
# character is found
def palindrome3(sf):
    start = -1
    for c in sf:
        if c == sf[start]:
            start = start - 1
        else:
            return False
    return True    

# palindrome check with for/range that
# returns immediatley when a non-matching
# character is found
def palindrome4(s1):
    for i in range(1, len(s1)):
        if s1[i-1] != s1[0-i]:
            return False
    return True


