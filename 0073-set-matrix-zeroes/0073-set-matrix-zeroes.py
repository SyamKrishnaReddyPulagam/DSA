class Solution:
    def setZeroes(self, m1: List[List[int]]) -> None:
        m=len(m1)
        n=len(m1[0])
        ans=[]
        for i in range(m):
            for j in range(n):
                if m1[i][j]==0:
                    ans.append([i,j])
        for k in ans:
            i,j=k[0],k[1]
            m1[i]=[0]*n
            for l in range(m):
                m1[l][j]=0
        return m1