class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if not right:
            return max(left)
        if not left:
            return n-min(right)
        return max(n-min(right),max(left))