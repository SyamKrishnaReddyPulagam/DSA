class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dicti=Counter(nums)
        n=max(dicti.values())
        ans=[[] for i in range(n)]
        dicti={}
        for i in nums:
            if i in dicti:
                dicti[i]+=1
            else:
                dicti[i]=1
            
            ans[dicti[i]-1].append(i)
        return ans