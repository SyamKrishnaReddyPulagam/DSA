class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        diff=[[0]*n]*m
        row=[0]*m
        col=[0]*n
        i,j=0,0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    row[i]+=1
                    col[j]+=1
        for i in range(m):
            for j in range(n):
                grid[i][j]=n-row[i]+m-col[j]-row[i]-col[j]
        return grid
        