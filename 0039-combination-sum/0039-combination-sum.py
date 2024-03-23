class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def func(i,tar,nums,arr):
            if i==len(nums):
                if tar==0:
                    ans.append(arr.copy())
                return
            if tar>=nums[i]:
                arr.append(nums[i])
                func(i,tar-nums[i],nums,arr)
                arr.pop()
                func(i+1,tar,nums,arr)
            else:
                func(i+1,tar,nums,arr)
        func(0,target,candidates,[])
        return ans