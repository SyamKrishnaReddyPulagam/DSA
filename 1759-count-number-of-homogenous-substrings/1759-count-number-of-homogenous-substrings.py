class Solution:
    def countHomogenous(self, s: str) -> int:
        ans=len(s)
        mod=(10**9)+7
        n=ans
        count=1
        i=1
        while i<n:
            if s[i]==s[i-1]:
                ans=(ans+count)%mod
                count+=1
            else:
                count=1
            i+=1
        return ans