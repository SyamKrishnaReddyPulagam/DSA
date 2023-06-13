class Solution(object):
    def findSpecialInteger(self, arr):
        n = len(arr)
        
        for i in [n//4, n//2, 3*n//4, n]:
            if arr[bisect.bisect_left(arr, arr[i]) + n//4] == arr[i]:
                return arr[i]