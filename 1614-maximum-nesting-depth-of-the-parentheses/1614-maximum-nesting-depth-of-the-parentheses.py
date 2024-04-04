class Solution:
    def maxDepth(self, s: str) -> int:
        op,cl=0,0
        ans=0
        for i in range(len(s)):
            if s[i]=="(":
                op+=1
            elif s[i]==")":
                cl+=1
            ans=max(ans,op-cl)
        return ans