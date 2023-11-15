class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        n=len(arr)
        if arr[0]!=1:
            arr[0]=1
        i=1
        while i<n:
            if arr[i]-arr[i-1]>1:
                arr[i]=arr[i-1]+1
            i+=1
        print(arr)
        return max(arr)