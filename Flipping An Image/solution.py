def flipAndInvertImage(self, A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    for row in range(len(A)):
        A[row] = A[row][::-1] # reverse the row

        for invert in range(len(A[row])): # invert each element
            if A[row][invert] == 0:
                A[row][invert] = 1
            else:
                A[row][invert] = 0
            
    return A    