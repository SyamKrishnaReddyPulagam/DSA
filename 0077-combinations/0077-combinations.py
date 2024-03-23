class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def func(nums,arr,i,k):
            if len(arr)==k:
                nonlocal ans
                ans.append(arr.copy())
                return
            if i==len(nums):
                return
            arr.append(nums[i])
            func(nums,arr,i+1,k)
            arr.pop()
            func(nums,arr,i+1,k)
        nums=[i for i in range(1,n+1)]
        func(nums,[],0,k)
        return ans