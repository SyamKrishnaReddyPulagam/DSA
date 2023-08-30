class Solution(object):
    def threeSumClosest(self, nums, target):
        m=float("inf")
        nums.sort()
        for i in range(len(nums)):
            j,k=i+1,len(nums)-1
            while j<k:
                x=nums[i]+nums[j]+nums[k]
                if abs(x - target) < abs(m - target):
                    m = x
                if x < target:
                    j += 1
                else:
                    k -= 1
        return m