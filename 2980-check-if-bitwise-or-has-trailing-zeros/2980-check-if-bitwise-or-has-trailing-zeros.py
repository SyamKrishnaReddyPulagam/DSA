class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        count=0
        i=0
        while i<len(nums):
            if nums[i]%2==0:
                count+=1
            if count==2:
                return True
            i+=1
        return False