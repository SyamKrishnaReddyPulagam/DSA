class Solution(object):
    def subtractProductAndSum(self, n):
        n=str(n)
        p=1
        s=0
        for i in n:
            p=p*int(i)
        for j in n:
            s=s+int(j)
        return p-s