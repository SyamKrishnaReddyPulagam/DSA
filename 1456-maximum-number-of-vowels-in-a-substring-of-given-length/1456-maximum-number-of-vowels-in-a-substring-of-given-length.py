class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow=['a','e','i','o','u']
        x=0
        ans=0
        for i in range(k):
            if s[i] in vow:
                x+=1
        ans=x
        for i in range(k,len(s)):
            if s[i] in vow:
                x+=1
            if s[i-k] in vow:
                x-=1
            ans=max(ans,x)
        return ans