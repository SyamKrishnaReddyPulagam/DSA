class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        a=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j,k=i+1,len(nums)-1
            while j<k:
                x=nums[i]+nums[j]+nums[k]
                if x>0:
                    k-=1
                elif x<0:
                    j+=1
                else:
                    a.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
        return a