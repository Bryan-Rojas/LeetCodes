def reverseVowels(self, s: str) -> str:
    l, r, s = 0, len(s)-1, list(s)
    vowels = 'aeiou'
    
    while l < r:
        while not s[l].lower() in vowels and l < r: l += 1
        while not s[r].lower() in vowels and l < r: r -= 1
                
        s[l], s[r] = s[r], s[l]
        
        l += 1
        r -= 1
        
    return ''.join(s)