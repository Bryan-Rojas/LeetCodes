def bitwiseComplement(self, N: int) -> int:
    digit, num = 1, N
    while N > 1:
        digit += 1
        N = N//2
    return 2**digit - 1 - num

"""
Example:
Input: 5, Output: 2
101, 010

digit
1 -> 2 -> 3

num
5

N
5 -> 2 -> 1

return (2 ^ 3) - 1 - 5 = 2
"""