class Solution:
    def reverseVowels(self, s: str) -> str:
        def repl(s,i,j):
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
