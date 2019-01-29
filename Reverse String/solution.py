def reverseString(s):
    """
    :type s: List[str]
    :rtype: void Do not return anything, modify s in-place instead.
    """
    l, r = 0, len(s) - 1
    while l <= r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

arr = ['B', 'r', 'y', 'a', 'n']

print(arr)
reverseString(arr)
print(arr)