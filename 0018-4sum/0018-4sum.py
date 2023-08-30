class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        a=[]
        i=0
        while i<len(nums)-3:
            j=i+1
            while j<len(nums)-2:
                k,l=j+1,len(nums)-1
                while k<l:
                    x=nums[i]+nums[j]+nums[k]+nums[l]
                    if x==target:
                        a.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        l -= 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif x < target:
                        k += 1
                    else:
                        l -= 1
                j += 1
                while j < len(nums) - 2 and nums[j] == nums[j - 1]:
                    j += 1
            i += 1
            while i < len(nums) - 3 and nums[i] == nums[i - 1]:
                i += 1
        return a