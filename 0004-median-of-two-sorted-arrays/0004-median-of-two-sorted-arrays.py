class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3=nums1 + nums2
        nums3= sorted(nums3)
        x = len(nums1) + len(nums2)
        if x%2==0:
            i=int(x/2)
            z=long(nums3[i-1]+ nums3[i])
            y=float(z)/2
            return y
        else:
            y=nums3[x/2]
            return y