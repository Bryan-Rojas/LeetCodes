#Newton Method
def isPerfectSquare(self, num: int) -> bool:
    r = num
    while r*r > num:
        r = (r + num/r) // 2
    return r*r == num

"""
#Bitwise Trick
def BitwiseTrick(self, num):
    root = 0
    bit = 1 << 15
    
    while bit > 0 :
        root |= bit
        if root > num // root:    
            root ^= bit                
        bit >>= 1        
    return root * root == num
"""

"""
#Binary Search Method
def BinarySearch(self, num):
    left = 0
    right = num
    
    while left <= right:
        mid = left + (right-left)//2
        if  mid ** 2 == num:
            return True
        elif mid ** 2 > num:
            right = mid -1
        else:
            left = mid +1
    return False
"""