class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        def func(i,tar,nums,arr,k):
            #print(arr)
            if len(arr)==k:
                if tar==0:
                    nonlocal ans
                    ans.append(arr.copy())
                return
            if i==9:
                return
            arr.append(nums[i])
            func(i+1,tar-nums[i],nums,arr,k)
            arr.pop()
            func(i+1,tar,nums,arr,k)
        nums=[i for i in range(1,10)]
        func(0,n,nums,[],k)
        return ans