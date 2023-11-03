class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        n=len(nums)
        while i<n-1:
            j=i+1
            while j<n:
                if nums[i]+nums[j]==target:
                    return [i,j]
                j+=1
            i+=1
        
        
            