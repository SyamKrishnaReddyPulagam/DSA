class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        dicti={}
        for i in range(n):
            dicti[i]=float("inf")
        dicti[0]=0
        edges={i:[i+1] for i in range(n)}
        edges[n-1]=[]
        def func(edges,dicti):
            for cur_node in range(n-1):
                for node in edges[cur_node]:
                    dicti[node]=min(dicti[node],dicti[cur_node]+1)
            return dicti
        ans=[]
        for i,j in queries:
            edges[i].append(j)
            dicti=func(edges,dicti)
            ans.append(dicti[n-1])
        return ans