class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(x[0],x[1]))
        temp=points[0]
        ans=[]
        for i in range(1,len(points)):
            if temp[1]<points[i][0]:
                ans.append(temp)
                temp=points[i]
            else:
                temp=[max(temp[0],points[i][0]),min(temp[1],points[i][1])]
        if temp not in ans:
            ans.append(temp)
        return len(ans)