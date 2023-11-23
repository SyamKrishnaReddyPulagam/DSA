class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def func(arr):
            arr.sort()
            n=len(arr)
            if n<=2:
                return True
            diff=arr[1]-arr[0]
            for i in range(1,n):
                if arr[i]-arr[i-1]!=diff:
                    return False
            return True
        m=len(l)
        i=0
        ans=[]
        while i<m:
            ans.append(func(nums[l[i]:r[i]+1]))
            i+=1
        return ans