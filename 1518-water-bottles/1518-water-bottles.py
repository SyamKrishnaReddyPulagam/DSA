class Solution:
    def numWaterBottles(self, bottle: int, req: int) -> int:
        ans=0
        full,empty=bottle,0
        while True:
            if full==0 and empty<req:
                break
            ans+=full
            empty+=full
            full=empty//req
            empty=empty%req
        return ans