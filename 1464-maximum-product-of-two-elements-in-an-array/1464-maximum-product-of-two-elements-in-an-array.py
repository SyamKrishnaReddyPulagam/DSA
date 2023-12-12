class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        z=heapq.nlargest(2,nums)
        ans=1
        for i in z:
            ans*=(i-1)
        return ans