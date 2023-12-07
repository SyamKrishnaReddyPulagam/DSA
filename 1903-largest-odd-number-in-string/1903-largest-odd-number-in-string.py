class Solution:
    def largestOddNumber(self, num: str) -> str:
        def odd(m):
            if int(m)%2==0:
                return False
            return True
        n=len(num)
        end=n-1
        while end>-1:
            if odd(num[end]):
                break
            end-=1
        if end==-1:
            return ""
        return num[:end+1]