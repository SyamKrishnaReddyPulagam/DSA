class Solution(object):
    def singleNonDuplicate(self, nums):
        i, j = 0, len(nums) // 2
        ans = -1
        while i <= j:
            mid = (i + j) // 2
            idx = mid * 2
            if idx + 1 >= len(nums) or nums[idx] != nums[idx + 1]:
                j = mid - 1
                ans = nums[idx]
            else:
                i = mid + 1
        return ans