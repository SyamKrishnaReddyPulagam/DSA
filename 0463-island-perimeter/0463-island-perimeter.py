class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited=set()
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    visited.add((i,j))
        ans=0
        for i,j in visited:
            x=0
            temp=[[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
            for a,b in temp:
                if 0<=a<m and 0<=b<n and (a,b) in visited:
                    x+=1
            ans+=4-x
        return ans