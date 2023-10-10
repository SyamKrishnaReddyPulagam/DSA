class Solution:
    def hIndex(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        print(nums)
        for i in range(len(nums)):
            if nums[i]>=n-i:
                return n-i
        return 0