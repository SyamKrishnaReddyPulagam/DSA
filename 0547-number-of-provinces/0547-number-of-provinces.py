class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node,visited,adj):
            visited[node]=1
            for i in adj[node]:
                if visited[i]==0:
                    dfs(i,visited,adj)
        adj={}
        for i in range(len(isConnected)):
            temp=[]
            for j in range(len(isConnected[i])):
                if isConnected[i][j]==1 and i!=j:
                    temp.append(j+1)
            adj[i+1]=temp
        ans=0
        visited=[0 for _ in range(len(isConnected)+1)]
        for i in range(1,len(isConnected)+1):
            if visited[i]==0:
                dfs(i,visited,adj)
                ans+=1
        return ans