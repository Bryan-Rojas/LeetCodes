def findWords(self, words: List[str]) -> List[str]:
        a=set('qwertyuiop')
        b=set('asdfghjkl')
        c=set('zxcvbnm')
        ans=[]
        for word in words:
            w=set(word.lower())
            if (a&w==w) | (b&w==w) | (c&w==w):
                ans.append(word)
        return ans