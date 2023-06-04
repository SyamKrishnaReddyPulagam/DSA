class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        a,b=0,0
        for i in nums:
            if i==1:
                a+=1
                b=max(a,b)
            else:
                a=0
        return b
        