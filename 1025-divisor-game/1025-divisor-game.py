class Solution:
    def divisorGame(self, n: int) -> bool:
        if n==1:
            return False
        dp=[0]*n
        for i in range(1,n):
            a=1+dp[i-1]
            if (i+1)%2==0:
                if (dp[i-1]+1)%2!=0 and a%2!=0:
                    dp[i]=min(a,dp[i-1]+1)
                elif (dp[i-1]+1)%2==0 and a%2!=0:
                    dp[i]=a
                elif (dp[i-1]+1)%2!=0 and a%2==0:
                    dp[i]=dp[i-1]+1
                else:
                    dp[i]=min(a,dp[i-1]+1)
            else:
                dp[i]=dp[i-1]+1
        if dp[-1]%2==0:
            return False
        return True