#First solution
"""
def reverseOnlyLetters(self, S: str) -> str:
    l, r = 0, len(S) - 1
    S = list(S)
    while l < r:
        while l < r and not S[l].isalpha(): l+=1
        while l < r and not S[r].isalpha(): r-=1
        
        if(S[l].isalpha() and S[r].isalpha()):
            S[l], S[r] = S[r], S[l]
        l+=1
        r-=1
        
    return ''.join(S)
"""

#Second solution
def reverseOnlyLetters(self, S: 'str') -> 'str':
    stack = []
    return_str = []

    for elem in S:
        if elem.isalpha():
            stack.append(elem)
    
    for elem in S:
        if elem.isalpha():
            return_str.append(stack.pop())
        else:
            return_str.append(elem)
    
    return ''.join(return_str)