class Solution:
    def countKeyChanges(self, s: str) -> int:
        n=len(s)
        i=1
        ans=0
        while i<n:
            if s[i]==s[i-1].lower() or s[i]==s[i-1].upper():
                i+=1
            else:
                ans+=1
                i+=1
        return ans