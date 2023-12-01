class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x:x[1])
        end,ans=intervals[0][0],0
        n=len(intervals)
        for i in range(n):
            if intervals[i][0]>=end:
                end=intervals[i][1]
            else:
                ans+=1
        return ans