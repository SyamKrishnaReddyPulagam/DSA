class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dicti=Counter(nums)
        arr=[[i,dicti[i]] for i in dicti]
        arr.sort(key=lambda x:(x[1],-x[0]))
        ans=[]
        for i in arr:
            for j in range(i[1]):
                ans.append(i[0])
        return ans