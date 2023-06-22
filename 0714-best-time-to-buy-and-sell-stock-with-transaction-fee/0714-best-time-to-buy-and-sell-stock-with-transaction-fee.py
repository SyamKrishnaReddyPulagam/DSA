class Solution(object):
    def maxProfit(self, prices, fee):
        free = 0
        hold = -prices[0]
        for i in prices:
            tmp = hold
            hold = max(hold, free - i)
            free = max(free, tmp + i - fee)
        return free