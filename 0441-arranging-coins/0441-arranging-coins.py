class Solution(object):
    def arrangeCoins(self, n):
        if(n==1):
            return 1
        x=1
        y=0
        while(n>=x):
            n=n-x
            x+=1
            y+=1
        return y