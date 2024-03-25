class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dicti1={}
        for i in nums:
            if i not in dicti1:
                dicti1[i]=1
            else:
                dicti1[i]+=1
        ans=[]
        for ele,fre in dicti1.items():
            if fre==2:
                ans.append(ele)
        return ans