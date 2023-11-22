class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans=[]
        n=len(nums)
        if n==1:
            return [x for x in nums[0]]
        for i in range(n-1,-1,-1):
            z=nums[i]
            for j in range(len(z)):
                ans.append((i+j,-i,z[j]))
        heapq.heapify(ans)
        x=len(ans)
        y=heapq.nsmallest(x,ans)
        return [i[2] for i in y ]