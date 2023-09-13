class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        minc=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                minc[i]=max(minc[i-1]+1,minc[i])
        for j in range(n-2,-1,-1):
            if ratings[j+1]<ratings[j]:
                minc[j]=max(minc[j+1]+1,minc[j])
        return sum(minc)