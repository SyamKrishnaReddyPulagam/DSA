class Solution(object):
    def countBits(self, n):
        a=[0]*(n+1)
        for i in range(n+1):
            x=bin(i).replace("0b", "")
            y=x.count("1")
            a[i]=y
        return a