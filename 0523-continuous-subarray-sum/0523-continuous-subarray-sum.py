class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dicti={0:-1}
        cursum=0
        for i in range(len(nums)):
            cursum+=nums[i]
            rem=cursum%k
            if rem not in dicti:
                dicti[rem]=i
            else:
                prev=dicti[rem]
                if i-prev>=2:
                    return True
        return False