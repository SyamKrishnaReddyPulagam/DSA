class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans=start ^ goal
        count=0
        while ans:
            if ans&1==1:
                count+=1
            ans>>=1
        return count