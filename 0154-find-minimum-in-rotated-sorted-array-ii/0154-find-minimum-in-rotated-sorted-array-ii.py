class Solution(object):
    def findMin(self, nums):
        a=[]
        [a.append(i) for i in nums if i not in a]
        left,right=0,len(a)-1
        while left<right:
            mid=(left+right)//2
            if a[mid]>a[right]:
                left=mid+1
            else:
                right=mid
        return a[left]