class Solution:
    def reverseVowels(self, s: str) -> str:
        """def repl(s,i,j):
            s=s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
            return s
        i,j=0,len(s)-1
        vow=["a","e","i","o","u","A", "E", "I", "O", "U"]
        while i<j:
            if s[i] in vow and s[j] in vow:
                s=repl(s,i,j)
                i+=1
                j-=1
            elif s[i] in vow:
                j-=1
            elif s[j] in vow:
                i+=1
            else:
                i+=1
                j-=1
        return s
    """
        s = list(s)
        left = 0
        right = len(s) - 1
        m = 'aeiouAEIOU'
        while left < right:
            if s[left] in m and s[right] in m:
                
                s[left], s[right] = s[right], s[left]
                
                left += 1; right -= 1
            
            elif s[left] not in m:
                left += 1
            
            elif s[right] not in m:
                right -= 1
            
        return ''.join(s)