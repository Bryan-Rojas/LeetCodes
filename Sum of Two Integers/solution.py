"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
"""
def getSum(a: 'int', b: 'int') -> 'int':
    if a == 0:
        return b
    if b == 0:
        return a

    temp = 0xffffffff

    while b != 0:
        a, b = (a ^ b) & temp, ((a & b) << 1) & temp

    if (a >> 31) & 1:
        return ~(a & temp)
    else:
        return a

    #Convert a and b into two's compliment.
    #Add both two's complements.
    #Convert back to integer.

    """
    Alternate solution:

    list = [a, b]
    return sum(list)

    """