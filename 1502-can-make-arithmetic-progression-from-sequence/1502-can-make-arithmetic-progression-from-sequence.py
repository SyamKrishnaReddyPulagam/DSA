class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        def insertionSort(arr,n):
            for i in range(1, n):
                key = arr[i]
                j = i-1
                while j >=0 and key < arr[j] :
                        arr[j+1] = arr[j]
                        j -= 1
                arr[j+1] = key
            return arr
        arr=insertionSort(arr,len(arr))
        for i in range(2,len(arr)):
            if arr[i]-arr[i-1]!=arr[1]-arr[0]:
                return False
        return True