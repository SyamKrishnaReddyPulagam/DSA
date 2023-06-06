class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(len(arr)):
            b = i * diff
            res = arr[0] + b
            if arr[i] != res:
                return False    
        return True
        