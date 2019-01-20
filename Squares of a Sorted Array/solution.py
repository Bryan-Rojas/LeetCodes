def sortedSquares(A):
    left, right, answers = 0, len(A)-1, []
    
    while left <= right:
        if(A[right]*A[right] > A[left]*A[left]):
            answers.append(A[right]*A[right])
            right -= 1
        else:
            answers.append(A[left]*A[left])
            left += 1
    return answers[::-1]

inputArr = [-4, -1, 0, 1, 3, 5]

print(sortedSquares(inputArr))