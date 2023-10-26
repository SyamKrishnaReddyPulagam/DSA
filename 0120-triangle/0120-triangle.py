class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        level=1
        i=0
        while level<n and i<level+1:
            if i==0:
                triangle[level][i]+=triangle[level-1][0]
                i+=1
            elif i==level:
                triangle[level][i]+=triangle[level-1][-1]
                level,i=level+1,0
            else:
                triangle[level][i]+=min(triangle[level-1][i-1],triangle[level-1][i])
                i+=1
        return min(triangle[-1])