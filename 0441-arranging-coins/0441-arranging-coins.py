class Solution(object):
    def arrangeCoins(self, n):
        if(n==1):
            return 1
        x=1
        while(n>=x):
            n=n-x
            x+=1
        return x-1