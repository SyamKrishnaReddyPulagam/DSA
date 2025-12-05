class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        pre_sum,tot=[],0
        for i in nums:
            tot+=i
            pre_sum.append(tot)
        ans=0
        for i in range(len(nums)-1):
            diff=2*pre_sum[i]-tot
            if diff%2==0:
                ans+=1
        return ans