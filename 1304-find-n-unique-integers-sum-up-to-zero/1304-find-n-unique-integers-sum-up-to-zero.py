class Solution(object):
    def sumZero(self, n):
        y=1
        z=0
        c=-1
        a=[]*n
        x=int(n/2)
        if n%2!=0:
            for i in range(x):
                a.append(y)
                y+=1
            for i in range(x,-1,-1):
                a.append(z)
                z-=1
        if n%2==0:
            for i in range(x):
                a.append(y)
                y+=1
            for i in range(x,n,1):
                a.append(c)
                c-=1
        return a
             