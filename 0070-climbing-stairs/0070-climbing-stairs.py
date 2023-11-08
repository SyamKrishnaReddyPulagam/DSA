class Solution:
    def climbStairs(self, n: int) -> int:
        if n<4:
            return n
        arr=[0]*(n+1)
        arr[-1]=1
        arr[-2]=1
        for i in range(n-2,-1,-1):
            arr[i]=arr[i+1]+arr[i+2]
        return arr[0]