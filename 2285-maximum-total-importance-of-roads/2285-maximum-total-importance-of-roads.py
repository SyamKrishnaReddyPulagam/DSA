class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        from sortedcontainers import SortedDict
        degree={i:0 for i in range(n)}
        for i,j in roads:
            degree[i]-=1
            degree[j]-=1
        temp=SortedDict()
        for i,j in degree.items():
            if j in temp:
                temp[j].append(i)
            else:
                temp[j]=[i]
        dicti={}
        for i in temp:
            for j in temp[i]:
                dicti[j]=n
                n-=1
        ans=0
        for i,j in roads:
            ans+=dicti[i]+dicti[j]
        return ans