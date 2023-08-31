class Solution(object):
    def minTaps(self, n, ranges):
        max,min=0,0
        open=0
        while max<n:
            for i in range(len(ranges)):
                if i-ranges[i]<=min and i+ranges[i]>max:
                    max=i+ranges[i]
            if min==max:
                return -1
            open+=1
            min=max
        return open