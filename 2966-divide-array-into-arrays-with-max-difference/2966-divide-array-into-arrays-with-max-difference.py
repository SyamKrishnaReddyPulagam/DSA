class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        i=2
        while i<n:
            if nums[i]-nums[i-2]<=k:
                i+=3
            else:
                print(i)
                return []
        temp=[nums[i:i+3]for i in range(0,n,3)]
        return temp