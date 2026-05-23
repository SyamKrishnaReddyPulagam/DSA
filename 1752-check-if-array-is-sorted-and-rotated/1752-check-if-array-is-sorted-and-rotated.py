class Solution:
    def check(self, nums: List[int]) -> bool:
        fall,cur,broken=False,nums[0],False
        for i in range(1,len(nums)):
            if nums[i]<cur and fall:
                broken=True
                return False
            elif nums[i]<cur:
                cur=nums[i]
                fall=True
            else:
                cur=nums[i]
        if not fall:
            return True
        if fall and not broken:
            if nums[-1]<=nums[0]:
                return True
        return False