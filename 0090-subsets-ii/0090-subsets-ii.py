class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        for n in nums:
            for i in range(len(result)):
                result.append(result[i]+[n])
        
        ans=[]
        [ans.append(i) for i in result if i not in ans]
        return ans