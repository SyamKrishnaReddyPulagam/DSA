class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        row,col=[],[]
        for i in range(m):
            temp=[]
            a=0
            for j in range(n):
                a+=grid[i][j]
                temp.append(a)
            row.append(temp)
        col=[[0 for i in range(n)] for j in range(m)]
        for j in range(n):
            a=0
            for i in range(m):
                a+=grid[i][j]
                col[i][j]=a
        ans=[[0 for i in range(n)]for j in range(m)]
        c=0
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    ans[i][j]=grid[i][j]
                elif i==0:
                    ans[i][j]=row[i][j]
                elif j==0:
                    ans[i][j]=col[i][j]
                else:
                    ans[i][j]=ans[i][j-1]+col[i][j]
        for i in range(m):
            for j in range(n):
                if ans[i][j]<=k:
                    c+=1
        return c