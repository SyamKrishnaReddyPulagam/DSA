class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if right and left:
            a1=max(left)
            a2=min(right)
            return max(n-a2,a1)
        elif not right:
            a1=max(left)
            return a1
        else:
            a2=min(right)
            return n-a2
        