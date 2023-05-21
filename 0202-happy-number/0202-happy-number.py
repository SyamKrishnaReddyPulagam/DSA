class Solution(object):
    def isHappy(self, n):
        if n>(2**31-1):
            return False
        for i in range(10):
            n=sum(int(x) ** 2 for x in str(n))
        if n==1:
            return True
        else:
            return False