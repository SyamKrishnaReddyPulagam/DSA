class Solution(object):
    def sortColors(self, nums):
        a,b,c=0,0,0
        for i in nums:
            if i==0:
                a+=1
            elif i==1:
                b+=1
            else:
                c+=1
        for i in range(a):
            nums[i]=0
        for i in range(b):
            nums[a+i]=1
        for i in range(c):
            nums[a+b+i]=2
        return nums