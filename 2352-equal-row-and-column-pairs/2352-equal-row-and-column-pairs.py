class Solution(object):
    def equalPairs(self, grid):
        n=len(grid)
        a=[]
        for i in range(n):
            a.append([row[i] for row in grid])
        k=0
        for i in range(n):
            for j in range(n):
                if grid[i]==a[j]:
                    k+=1
        return k