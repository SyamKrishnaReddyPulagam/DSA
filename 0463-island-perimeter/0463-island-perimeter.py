class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited=set()
        dicti={}
        m,n=len(grid),len(grid[0])
        def func(i,j,grid):
            visited.add((i,j))
            dicti[(i,j)]=0
            temp=[[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
            for i,j in temp:
                if 0<=i<m and 0<=j<n and grid[i][j]==1 and (i,j) not in visited:
                    func(i,j,grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in visited:
                    func(i,j,grid)
                    break
        ans=0
        for i,j in visited:
            x=0
            temp=[[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
            for a,b in temp:
                if 0<=a<m and 0<=b<n and (a,b) in visited:
                    x+=1
            ans+=4-x
        return ans