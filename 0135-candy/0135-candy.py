class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        min_can=1*n
        minc=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                min_can-=minc[i]
                minc[i]=max(minc[i-1]+1,minc[i])
                min_can+=minc[i]
        for j in range(n-2,-1,-1):
            if ratings[j+1]<ratings[j]:
                min_can-=minc[j]
                minc[j]=max(minc[j+1]+1,minc[j])
                min_can+=minc[j]
        return min_can
        