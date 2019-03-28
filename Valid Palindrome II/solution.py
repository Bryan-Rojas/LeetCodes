"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
"""
def validPalindrome(self, s: str) -> bool:
    sReversed=s[::-1]
    if s==sReversed:
        return True
    
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            one, two = s[left:right], s[left + 1:right + 1]
            return one == one[::-1] or two == two[::-1]
        left, right = left + 1, right - 1
    return True