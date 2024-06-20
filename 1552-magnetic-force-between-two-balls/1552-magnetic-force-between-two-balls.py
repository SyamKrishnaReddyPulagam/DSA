class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n=len(position)
        position.sort()
        def func(position,a,m):
            count,prev=1,0
            for i in range(1,len(position)):
                if position[i]-position[prev]>=a:
                    count+=1
                    prev=i
            return count>=m
        left,right=0,max(position)-min(position)
        ans=-1
        while left<=right:
            mid=(left+right)//2
            if func(position,mid,m):
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans