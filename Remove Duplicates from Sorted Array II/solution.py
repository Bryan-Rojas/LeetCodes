def removeDuplicates(self, nums: List[int]) -> int:
    n = len(nums) 
    if n<=2:
        return n
    else:
        t = 0
        cnt = 1
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                cnt = cnt+1
                if cnt<=2:
                    t = t+1
                    nums[t] = nums[i]
            else:
                t = t+1
                nums[t] = nums[i]
                cnt = 1
        return t+1