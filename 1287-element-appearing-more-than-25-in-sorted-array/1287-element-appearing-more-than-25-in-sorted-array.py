class Solution(object):
    def findSpecialInteger(self, arr):
        n=len(arr)//4
        for i in range(len(arr)):
            c=arr.count(arr[i])
            if c>n:
                return arr[i]
            