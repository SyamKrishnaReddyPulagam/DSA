class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        temp=[[i,j] for i,j in zip(capital,profits)]
        heapq.heapify(temp)
        maxi=[]
        heapq.heapify(maxi)
        for i in range(k):
            while temp and temp[0][0]<=w:
                a,b=heapq.heappop(temp)
                heapq.heappush(maxi,-b)
            if not maxi:
                break
            w+=-1*heapq.heappop(maxi)
        return w