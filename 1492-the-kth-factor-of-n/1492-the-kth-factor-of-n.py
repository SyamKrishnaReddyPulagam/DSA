class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        arr=[]
        for i in range(0,(n//2)):
            if n%(i+1)==0:
                arr.append(i+1)
        arr.append(n)
        if k>len(arr):
            return -1
        return arr[k-1]