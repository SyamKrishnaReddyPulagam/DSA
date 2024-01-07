class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp=[1]
        a,b,c=0,0,0
        while n>1:
            x,y,z=2*dp[a],3*dp[b],5*dp[c]
            ele=min(x,y,z)
            if ele==x:
                a+=1
            if ele==y:
                b+=1
            if ele==z:
                c+=1
            dp.append(ele)
            n-=1
        return dp[-1]