class Solution(object):
    def peakIndexInMountainArray(self, arr):
        for i in range(len(arr)-1):
            if arr[i+1]<arr[i]:
                return i