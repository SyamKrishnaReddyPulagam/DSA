class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])

        count=[[0]*n for _ in range(m)]
        for j in range(n):
            for i in range(m-1,-1,-1):
                if matrix[i][j]:
                    count[i][j]=1
                    if i<m-1:
                        count[i][j]+=count[i+1][j]
        ans=0
        for i in range(m):
            sortedcount=sorted(count[i],reverse=True)
            for j in range(n):
                ans=max(ans,sortedcount[j]*(j+1))
        return ans