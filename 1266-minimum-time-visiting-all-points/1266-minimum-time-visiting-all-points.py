class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        m=0
        for i in range(len(points)-1):
            m+=max(abs(points[i+1][0]-points[i][0]),abs(points[i+1][1]-points[i][1]))
        return m
                