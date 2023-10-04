class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        i=0
        j=len(costs)-1
        a,b=[],[]
        ans=0
        while k>0:
            while len(a)<candidates and i<=j:
                heapq.heappush(a,costs[i])
                i+=1
            while len(b)<candidates and i<=j:
                heapq.heappush(b,costs[j])
                j-=1
            a1=a[0] if a else float("inf")
            b1=b[0] if b else float("inf")
            if a1<=b1:
                ans+=a1
                heapq.heappop(a)
            else:
                ans+=b1
                heapq.heappop(b)
            k-=1
        return ans