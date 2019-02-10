def missingNumber(nums: 'List[int]') -> 'int':
    exists = []
    for x in range(0, len(nums)+1):
        exists.append(x)
    return sum(exists)-sum(nums)

Input = [9,6,4,2,3,5,7,0,1]
print(missingNumber(Input))