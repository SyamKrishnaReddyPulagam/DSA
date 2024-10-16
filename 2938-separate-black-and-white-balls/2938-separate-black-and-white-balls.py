class Solution:
    def minimumSteps(self, s: str) -> int:
        n=len(s)
        i=n-1
        while i>=0:
            if s[i]=="0":
                break
            else:
                i-=1
        ans,j=0,i-1
        while j>=0:
            if s[j]=="1":
                ans+=i-j
                i-=1
            j-=1
        return ans