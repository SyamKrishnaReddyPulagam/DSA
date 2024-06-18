class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        dicti,ans=defaultdict(int),0
        for i in hours:
            cur_extra=i%24
            if cur_extra>0:
                ans+=dicti[24-cur_extra]
                dicti[cur_extra]+=1
            else:
                ans+=dicti[0]
                dicti[0]+=1
        return ans