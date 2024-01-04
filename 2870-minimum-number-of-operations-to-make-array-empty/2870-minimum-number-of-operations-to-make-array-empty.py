class Solution:
    def minOperations(self, nums: List[int]) -> int:
        arr=Counter(nums)
        opr=0
        if min(arr.values())==1:
            return -1
        for i in arr.values():
            if i==2 or i==3:
                opr+=1
            else:
                opr+=i//3+(i%3!=0)
        return opr