class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        dels = cnt = 0

        for i in range(n - 1):
            if (cnt % 2) == 0 and (nums[i] == nums[i + 1]):
                dels += 1
            else:
                cnt += 1
                
        cnt += 1         
        dels += cnt & 1  
        return dels