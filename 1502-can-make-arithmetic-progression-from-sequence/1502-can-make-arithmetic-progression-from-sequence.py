class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        N = len(arr)
        a = arr[0]
        diff = arr[1] - a
        for i in range(N):
            a = a
            b = i * diff
            res = a + b
            if arr[i] != res:
                return False    
        return True
        