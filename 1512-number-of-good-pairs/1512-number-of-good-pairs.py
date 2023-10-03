class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a=Counter(nums)
        n=0
        for i in a.values():
            if i>1:
                n+=(i*(i-1))//2
        return n