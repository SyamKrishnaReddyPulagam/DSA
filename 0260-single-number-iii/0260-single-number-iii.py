class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dicti=Counter(nums)
        ans=[]
        for i in nums:
            if dicti[i]==1:
                ans.append(i)
        return ans