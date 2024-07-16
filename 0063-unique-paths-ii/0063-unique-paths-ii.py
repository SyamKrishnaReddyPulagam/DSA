class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        if grid[-1][-1]==1:
            return 0
        m,n=len(grid),len(grid[0])
        dp=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(m-1,-1,-1):
            if grid[i][-1]==1:
                break
            else:
                dp[i][-1]=1
        for j in range(n-1,-1,-1):
            if grid[m-1][j]==1:
                break
            else:
                dp[m-1][j]=1
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if grid[i][j]!=1:
                    dp[i][j]=dp[i+1][j]+dp[i][j+1]
        return dp[0][0]