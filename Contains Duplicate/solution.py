def containsDuplicate(nums: 'List[int]') -> 'bool':
    """
    nums type: List[ints]
    rtype: bool
    """
    return len(nums) != len(set(nums))

    