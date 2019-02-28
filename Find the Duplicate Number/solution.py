def findDuplicate(self, nums: List[int]) -> int:
    empty = set()
    
    for item in nums:
        if item in empty:
            return item
        else:
            empty.add(item)