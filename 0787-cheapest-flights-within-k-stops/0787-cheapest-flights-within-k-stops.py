class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ans=[float("inf")]*n
        ans[src]=0
        for i in range(k+1):
            temp=ans.copy()
            for s,d,c in flights:
                if ans[s]==float("inf"):
                    continue
                if ans[s] + c < temp[d]:
                    temp[d]=ans[s]+c
            ans=temp
        if ans[dst]==float("inf"):
            return -1
        return ans[dst]