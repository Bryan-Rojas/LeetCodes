def removeDuplicates(nums: 'List[int]') -> 'int':
    if not nums:
        return 0

    newTail = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[newTail]:
            newTail += 1
            nums[newTail] = nums[i]

    return newTail + 1

nums = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(nums))
print(nums)