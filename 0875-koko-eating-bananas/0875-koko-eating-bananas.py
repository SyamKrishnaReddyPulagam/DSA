class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        ans=0
        while l<=r:
            mid=(l+r)//2
            cache=0
            for i in piles:
                cache+=math.ceil(i/mid)
                if cache>h:
                    break
            if cache>h:
                l=mid+1
            else:
                ans=mid
                r=mid-1
        return ans