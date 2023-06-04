class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        a=[]
        for i in range(len(nums)):
            if nums[i]==1:
                a.append(i)
        if a==[]:
            return 0
        i=0
        b=0
        c=0
        while i<len(a)-1:
            if a[i]+1==a[i+1]:
                b+=1
            else:
                b=0
            c=max(c,b)
            i+=1
        return c+1
        