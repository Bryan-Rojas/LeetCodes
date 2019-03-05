# https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
# The problem, widely known as digit root problem, has a congruence formula:

"""
For base b (decimal case b = 10), the digit root of an integer is:

dr(n) = 0 if n == 0
dr(n) = (b-1) if n != 0 and n % (b-1) == 0
dr(n) = n mod (b-1) if n % (b-1) != 0
or

dr(n) = 1 + (n - 1) % 9
Note here, when n = 0, since (n - 1) % 9 = -1, the return value is zero (correct).

From the formula, we can find that the result of this problem is immanently periodic, with period (b-1).

Output sequence for decimals (b = 10):

~input: 0 1 2 3 4 ...
output: 0 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 ....

Henceforth, we can write the following code, whose time and space complexities are both O(1).
"""

def addDigits(self, num: int) -> int:
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9

#OR (faster by a couple milliseconds)

"""
def addDigits(self, num: 'int') -> 'int':
    while num // 10 > 0:
        s = 0
        while num > 0:
            s += num % 10
            num //= 10
        num = s
    return num
"""