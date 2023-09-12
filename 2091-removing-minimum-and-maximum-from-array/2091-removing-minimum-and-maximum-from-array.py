class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maxi=max(nums)
        mini=min(nums)
        i=nums.index(maxi)
        j=nums.index(mini)
        n=len(nums)
        x=max(i,j)
        y=min(i,j)
        print(x,y)
        return min(x+1,n-y,y+n-x+1)