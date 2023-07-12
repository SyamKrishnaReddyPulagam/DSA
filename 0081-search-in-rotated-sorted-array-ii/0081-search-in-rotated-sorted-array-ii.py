class Solution(object):
    def search(self, nums, target):
        nums1=[]
        [nums1.append(i) for i in nums if i not in nums1]
        def s(a,b,nums1,target):
            for i in range(a,b,1):
                if nums1[i]==target:
                    return True
            return False
        minm=float('inf')
        a=0
        for i in range(len(nums1)):
            if nums1[i]<minm:
                minm=nums1[i]
                a=i
        print(a)
        if minm==nums1[0] :
            return s(0,len(nums1),nums1,target)
        if(target>=nums1[0]):
            return s(0,a,nums1,target)
        else:
            return s(a,len(nums1),nums1,target)