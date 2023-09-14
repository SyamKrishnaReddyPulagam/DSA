class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """nums.sort()
        res, l, r = 0, 0 ,len(nums) - 1

        while l < r:
            S = nums[l] + nums[r]
            if S > k:
                r -= 1
            elif S < k:
                l += 1
            else:
                res += 1
                l += 1
                r -= 1
        return res
        """
        pair = defaultdict(int)
        res = 0
        
        for n in nums:
            if pair[n]: 
                res += 1
                pair[n] -= 1
            else: 
                pair[k - n] += 1
                
        return res