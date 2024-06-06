class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize!=0:
            return False
        dicti=Counter(hand)
        hand=list(set(hand))
        heapq.heapify(hand)
        while hand:
            temp=heapq.nsmallest(groupSize,hand)
            if len(temp)<groupSize:
                return False
            for i in range(1,groupSize):
                if temp[i]-1!=temp[i-1]:
                    return False
            for i in temp:
                dicti[i]-=1
                if dicti[i]==0:
                    del dicti[i]
                    t=heapq.heappop(hand)
                    if t!=i:
                        return False
        return True