class Solution(object):
    def findDifferentBinaryString(self, nums):
        n=len(nums)
        arr=""
        for i in range(n):
            if nums[i][i]=="0":
                arr+="1"
            else:
                arr+="0"
        return arr