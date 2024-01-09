class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans=0
        xor=nums[0]
        for i in range(1,len(nums)):
            xor=xor^nums[i]
        xor=xor^k
        return bin(xor).count("1")