class Solution(object):
    def countKeyChanges(self, s):
        s=lower(s)
        n=len(s)
        i=1
        ans=0
        while i<n:
            if s[i]!=s[i-1]:
                ans+=1
            i+=1
        return ans