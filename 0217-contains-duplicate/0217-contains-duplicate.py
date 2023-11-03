class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset=Counter(nums)
        for i in hashset:
            if hashset[i]>1:
                return True
        return False