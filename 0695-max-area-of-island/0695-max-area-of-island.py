class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans=0
        m,n=len(grid),len(grid[0])
        visited=[[False for _ in range(n)]for _ in range(m)]
        def bfs(row,col,grid,visited,cache):
            visited[row][col]=True
            queue=deque()
            queue.append([row,col])
            cache[0]+=1
            while queue:
                for i in range(len(queue)):
                    a,b=queue.popleft()
                    arr=[[a,b-1],[a,b+1],[a+1,b],[a-1,b]]
                    for r,c in arr:
                        if 0<=r<m and 0<=c<n and visited[r][c]==False and grid[r][c]==1:
                            visited[r][c]=True
                            queue.append([r,c])
                            cache[0]+=1
            return cache
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and not visited[i][j]:
                    cache=[0]
                    bfs(i,j,grid,visited,cache)
                    ans=max(ans,cache[0])
        return ans