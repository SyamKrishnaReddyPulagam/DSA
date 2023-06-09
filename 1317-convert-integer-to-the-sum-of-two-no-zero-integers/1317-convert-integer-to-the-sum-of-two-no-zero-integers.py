class Solution(object):
    def check_zeros(self,n):
        while(n>0):
            lsb=n%10
            if lsb==0:
                return False
            n=int(n/10)
        return True
    def getNoZeroIntegers(self, n):
        a=1
        while(True):
            b=n-a
            if self.check_zeros(a) and self.check_zeros(b):
                return [a,b]
            a=a+1