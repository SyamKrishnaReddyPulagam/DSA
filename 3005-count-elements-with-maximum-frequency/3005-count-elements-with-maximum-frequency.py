class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash1=Counter(nums)
        max_fre=max(hash1.values())
        ans=0
        for i in hash1:
            if hash1[i]==max_fre:
                ans+=max_fre
        return ans