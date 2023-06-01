class Solution(object):
    def myPow(self, x, n):
        if n==0:
            return 1
        elif n==1:
            return x
        else:
            if n<0:
                n=abs(n)
                x=1/x
            if n%2==0:
                return self.myPow(x*x,n/2)
            else:
                return x*self.myPow(x*x,n/2)
       