class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        """m,n=len(nums1),len(nums2)
        i,j=0,0
        while i<m and j<n:
            if nums1[i]==nums2[j]:
                return nums1[i]
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return -1"""
        a=set(nums1) & set(nums2)
        if not a:
            return -1
        return min(a)