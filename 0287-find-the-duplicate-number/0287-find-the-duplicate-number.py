class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashset=collections.Counter(nums)
        for i in nums:
            if hashset[i]>1:
                return i