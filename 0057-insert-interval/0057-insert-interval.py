class Solution(object):
    def insert(self, intervals, newInterval):
        def mergeintervals(arr):
            a=[]
            for i in range(len(arr)):
                if len(a)==0 or a[len(a)-1][1]<arr[i][0]:
                    a.append(arr[i])
                else:
                    a[len(a)-1][1]=max(a[len(a)-1][1],arr[i][1])
            return a
        intervals.append(newInterval)
        intervals=sorted(intervals,key=lambda x:x[0])
        intervals=mergeintervals(intervals)
        return intervals