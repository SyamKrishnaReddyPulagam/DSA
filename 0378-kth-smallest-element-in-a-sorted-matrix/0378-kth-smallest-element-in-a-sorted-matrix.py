class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr=[]
        n=len(matrix)
        for i in range(n):
            arr+=matrix[i]
        heapq.heapify(arr)
        return heapq.nsmallest(k,arr)[-1]