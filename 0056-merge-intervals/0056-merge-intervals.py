class Solution(object):
    def merge(self, intervals):
        intervals=sorted(intervals,key=lambda x:x[0])
        a=[]
        for i in range(len(intervals)):
            if len(a)==0 or a[len(a)-1][1]<intervals[i][0]:
                a.append(intervals[i])
            else:
                a[len(a)-1][1]=max(a[len(a)-1][1],intervals[i][1])
        return a
            