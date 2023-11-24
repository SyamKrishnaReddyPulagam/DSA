class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        z=len(piles)//3
        x=-2
        ans=0
        while z!=0:
            ans+=piles[x]
            x-=2
            z-=1
        return ans