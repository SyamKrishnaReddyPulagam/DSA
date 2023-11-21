class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones)>=2:
            x,y=stones[-2],stones[-1]
            stones=stones[:-2]
            if x!=y:
                ap=y-x
                stones.append(ap)
                stones.sort()
            #print(stones)
        if stones:
            return stones[0]
        return 0