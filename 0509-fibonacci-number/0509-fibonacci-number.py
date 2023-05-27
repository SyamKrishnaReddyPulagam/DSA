class Solution(object):
    def fib(self, n):
        if(n<2):
            return n
        a=[0]*n
        a[0]=0
        a[1]=1
        for i in range(2,n):
            a[i]=a[i-1]+a[i-2]
        return a[n-1]+a[n-2]