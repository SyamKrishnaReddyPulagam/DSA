class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m,n=len(land),len(land[0])
        def dfs(i,j,land,visited):
            temp=[]
            visited.add((i,j))
            queue=deque()
            queue.append([i,j])
            temp.append([i,j])
            while queue:
                for _ in range(len(queue)):
                    node=queue.popleft()
                    i,j=node
                    cache=[[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
                    for x,y in cache:
                        if 0<=x<m and 0<=y<n and land[x][y]==1 and (x,y) not in visited:
                            visited.add((x,y))
                            queue.append([x,y])
                            temp.append([x,y])
            return temp,visited
        key=set()
        adj=[]
        ans=[]
        for i in range(m):
            for j in range(n):
                if land[i][j]==1:
                    adj.append([i,j])
        for i,j in adj:
            if (i,j) not in key:
                val,key=dfs(i,j,land,key)
                if val:
                    val.sort(key=lambda x:(x[0],x[1]))
                    ans.append([val[0][0],val[0][1],val[-1][0],val[-1][1]])
        return ans