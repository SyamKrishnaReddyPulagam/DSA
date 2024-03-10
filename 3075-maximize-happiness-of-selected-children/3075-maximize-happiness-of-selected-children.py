class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        nums=[]
        heapq.heapify(nums)
        for i in happiness:
            heapq.heappush(nums,-i)
        ans,a=0,0
        while k>0:
            ans+=max(0,(heapq.heappop(nums)*-1)-a)
            k,a=k-1,a+1
        return ans