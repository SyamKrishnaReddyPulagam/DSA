class Solution(object):
    def arrangeCoins(self, n):
        return int((-1 + sqrt(8 * n + 1)) // 2)
    