class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numRows=rowIndex+1
        nums=[]
        for i in range(1,numRows+1):
            x=[1]*i
            nums.append(x)
        for i in range(2,len(nums)):
            y=nums[i]
            for j in range(1,len(y)-1):
                nums[i][j]=nums[i-1][j-1]+nums[i-1][j]
        return nums[rowIndex]