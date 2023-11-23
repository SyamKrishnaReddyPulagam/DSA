class Solution:
    def isHappy(self, n: int) -> bool:
        z=set()
        sum1=0
        while sum1!=1:
            sum1=sum([ int(i)**2 for i in str(n)])
            n=sum1
            if sum1 in z:
                return False
            else:
                z.add(sum1)
        return True