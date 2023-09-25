class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a=Counter(s)
        b=Counter(t)
        ans=b-a
        ans=dict(ans)
        return next(iter(ans))