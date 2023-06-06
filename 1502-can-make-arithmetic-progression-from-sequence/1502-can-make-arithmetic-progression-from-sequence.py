class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        return len(set(arr[i-1] - arr[i] for i in range(1, len(arr)))) == 1