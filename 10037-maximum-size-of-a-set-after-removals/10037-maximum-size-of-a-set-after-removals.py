class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        nums1,nums2=set(nums1),set(nums2)
        nums=nums1&nums2
        nums=list(nums)
        while len(nums1)>n/2 and len(nums)>0:
            nums1.remove(nums[-1])
            nums.pop()
        while len(nums2)>n/2 and len(nums)>0:
            nums2.remove(nums[-1])
            nums.pop()
        while len(nums1)>n/2:
            nums1.pop()
        while len(nums2)>n/2:
            nums2.pop()
        return len(list(nums1.union(nums2)))
            