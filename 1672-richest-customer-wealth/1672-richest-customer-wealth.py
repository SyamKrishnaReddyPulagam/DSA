class Solution(object):
    def maximumWealth(self, accounts):
        richest_wealth=0
        x=len(accounts)
        y=len(accounts[0])
        for i in range(0,x):
            sum=0
            for j in range(0,y):
                sum+=accounts[i][j]
                if j==y-1 and sum>richest_wealth:
                    richest_wealth=sum
                    sum=0
        return richest_wealth