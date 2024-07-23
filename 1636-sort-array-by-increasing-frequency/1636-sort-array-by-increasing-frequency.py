class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dicti=Counter(nums)
        nums.sort(key=lambda x:[dicti[x],-x])
        return nums