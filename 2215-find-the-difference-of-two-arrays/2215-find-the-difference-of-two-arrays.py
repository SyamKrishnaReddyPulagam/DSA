class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1=collections.Counter(nums1)
        set2=collections.Counter(nums2)
        a=[]
        b=[]
        for i in nums1:
            if set2[i]==0 and i not in a:
                a.append(i) 
        for i in nums2:
            if set1[i]==0 and i not in b:
                b.append(i) 
        ans=[a,b]
        return ans