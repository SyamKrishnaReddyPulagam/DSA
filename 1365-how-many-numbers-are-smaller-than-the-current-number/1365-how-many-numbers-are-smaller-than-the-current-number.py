class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums1=nums.copy()
        nums1.sort()
        print(nums1)
        ans=[]
        for i in nums:
            j=nums1.index(i)
            ans.append(j)
        return ans