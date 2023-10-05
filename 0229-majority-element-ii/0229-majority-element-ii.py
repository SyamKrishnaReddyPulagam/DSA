class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums1=Counter(nums)
        print(nums1)
        n=len(nums)//3
        arr=[]
        for i,j in nums1.items():
            if j>n:
                arr.append(i)
        return arr