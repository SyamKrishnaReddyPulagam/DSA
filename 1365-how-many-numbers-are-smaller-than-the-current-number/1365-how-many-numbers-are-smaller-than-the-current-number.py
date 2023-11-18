class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums1=nums.copy()
        nums1.sort()
        count=0
        dicti={}
        for i in nums1:
            if i not in dicti:
                dicti[i]=count
                count+=1
            else:
                count+=1
        ans=[]
        for i in nums:
            ans.append(dicti[i])
        return ans