class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        start=[]
        m,n=len(grid),len(grid[0])
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    start.append([i,j])
        visited=[[False for _ in range(len(grid[0]))]for _ in range(len(grid))]
        def bfs(start,grid,visited):
            visited[start[0]][start[1]]=True
            queue=deque()
            queue.append(start)
            while queue:
                for i in range(len(queue)):
                    a,b=queue.popleft()
                    temp=[[a,b-1],[a,b+1],[a-1,b],[a+1,b]]
                    for i,j in temp:
                        if i>=0 and j>=0 and i<m and j<n and grid[i][j]=="1" and visited[i][j]==False:
                            visited[i][j]=True
                            queue.append([i,j])
        for i,j in start:
            if visited[i][j]==False:
                ans+=1
                bfs([i,j],grid,visited)
        return ans
        
                    