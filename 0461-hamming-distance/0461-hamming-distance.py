class Solution(object):
    def hammingDistance(self, x, y):
        x=bin(x).replace("0b", "")
        y=bin(y).replace("0b", "")
        x=str(x)
        y=str(y)
        j=0
        if len(x)>len(y):
            y=y.zfill(len(x))
        elif len(y)>len(x):
            x=x.zfill(len(y))
        for i in range(len(x)):
            if x[i]!=y[i]:
                j+=1
        return j