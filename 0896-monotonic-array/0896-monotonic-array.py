class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        x=sorted(nums)
        if nums== x or nums[::-1]==x:
            return True
        return False