def singleNumber(nums: 'List[int]') -> 'int':
    nums.sort()
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            i+=2
        else:
            return nums[i]
    return nums[-1]

input1 = [2,2,1]
input2 = [4,1,2,1,2]

print(singleNumber(input1))
print(singleNumber(input2))