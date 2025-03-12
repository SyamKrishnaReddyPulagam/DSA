class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans, cur_sum = 0, 0
        sum_count = defaultdict(int)
        sum_count[0] = 1  # For subarrays that sum to k from the start
        
        for num in nums:
            cur_sum += num
            if cur_sum - k in sum_count:
                ans += sum_count[cur_sum - k]
            sum_count[cur_sum] += 1
        
        return ans