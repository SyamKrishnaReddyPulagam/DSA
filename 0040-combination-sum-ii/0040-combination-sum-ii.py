class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def func(i,n,nums,tar,arr):
            if tar==0:
                nonlocal ans
                ans.append(arr.copy())
                return
            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                if nums[j]>tar:
                    break
                arr.append(nums[j])
                func(j+1,n,nums,tar-nums[j],arr)
                arr.pop()
            
        func(0,len(candidates),sorted(candidates),target,[])
        return ans