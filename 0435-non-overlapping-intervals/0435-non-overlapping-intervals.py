class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: (x[0],x[1]))

        n=len(intervals)
        a=[]
        count=0
        for i in range(n):
            if len(a)==0 or a[len(a)-1][1]<=intervals[i][0]:
                a.append(intervals[i])
            else:
                if intervals[i][1] < a[-1][1]:
                    a[-1] = intervals[i]
                count += 1
        return count
        