class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        arr=[]
        n=len(nums)
        prefix=[0]*n
        cache=0
        for i in range(n):
            cache+=nums[i]
            prefix[i]=cache
        for i in range(n):
            if i==0:
                arr.append(prefix[n-1]-prefix[0]-(nums[0]*(n-1)))
            elif i==n-1:
                arr.append((nums[i]*i)-prefix[i-1])
            else:
                arr.append(((nums[i]*i)-prefix[i-1])+((prefix[n-1]-prefix[i])-(nums[i]*(n-1-i))))
        return arr