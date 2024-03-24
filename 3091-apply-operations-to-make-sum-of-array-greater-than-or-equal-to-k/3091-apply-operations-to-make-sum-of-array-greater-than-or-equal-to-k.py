class Solution:
    def minOperations(self, k: int) -> int:
        ans=k
        if k==1:
            return 0
        if k==2:
            return 1
        for i in range(2,k):
            a=math.ceil(k/i)
            ans=min(ans,(i-1)+a-1)
        return ans