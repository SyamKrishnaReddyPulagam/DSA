class Solution(object):
    def maximumProduct(self, nums, k):
        mod=10**9 + 7
        heapq.heapify(nums)
        for i in range(k):
            heapq.heappushpop(nums,nums[0]+1)
        x=1
        for i in nums:
            x=(x*i)%mod
        return x