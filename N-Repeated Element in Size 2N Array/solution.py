def repeatedNTimes(A):
    seen = set()
    for i in A:
        if(i in seen):
            return i
        else:
            seen.add(i)

arr1 = [5,1,5,2,5,3,5,4]
arr2 = [2,1,2,5,3,2]

print(repeatedNTimes(arr1))
print(repeatedNTimes(arr2))