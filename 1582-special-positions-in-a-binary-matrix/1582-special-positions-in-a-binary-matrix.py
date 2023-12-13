class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m,n=len(mat),len(mat[0])
        row=[0]*m
        col=[0]*n
        i,j=0,0
        ans=0
        while i<m:
            if mat[i][j]==1:
                row[i]+=1
                col[j]+=1
            if j==n-1:
                j=0
                i+=1
            else:
                j+=1
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1 and row[i]==1 and col[j]==1:
                    ans+=1
        return ans