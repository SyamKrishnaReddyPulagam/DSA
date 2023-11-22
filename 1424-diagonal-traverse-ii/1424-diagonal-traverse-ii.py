class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        dicti=defaultdict(list)
        n=len(nums)
        if n==1:
            return nums[0]
        for i in range(n):
            rowi=nums[i]
            for j in range(len(rowi)):
                dicti[i+j]=[nums[i][j]]+dicti[i+j]
        final=[]
        z=dicti.values()
        for i in z:
            final+=i
        return final