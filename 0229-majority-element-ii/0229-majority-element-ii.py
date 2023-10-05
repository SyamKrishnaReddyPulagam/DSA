class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums1=Counter(nums)
        n=len(nums)//3
        arr=[]
        for i in nums1:
            if nums1[i]>n:
                arr.append(i)
        return arr