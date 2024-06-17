class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        temp=set()
        for i in range(int(sqrt(c))+1):
            temp.add(i**2)
        for i in temp:
            if c-i in temp:
                return True
        return False