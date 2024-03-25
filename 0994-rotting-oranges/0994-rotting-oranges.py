class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(start,grid,visited,ans):
            queue=deque()
            for row,col in start:
                visited[row][col]=True
                queue.append([row,col])
            while queue:
                ans[0]+=1
                for i in range(len(queue)):
                    a,b=queue.popleft()
                    arr=[[a,b-1],[a,b+1],[a+1,b],[a-1,b]]
                    for r,c in arr:
                        if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c]==1 and not visited[r][c]:
                            fresh.remove((r,c))
                            visited[r][c]=True
                            queue.append([r,c])
            return ans[0]
        visited=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        start,fresh=[],set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh.add((i,j))
                if grid[i][j]==2:
                    start.append([i,j])
        ans=[-1]
        if not fresh:
            return 0
        for ro,co in start:
            if not visited[ro][co]:
                bfs(start,grid,visited,ans)
        if fresh:
            return -1
        return ans[0]
        