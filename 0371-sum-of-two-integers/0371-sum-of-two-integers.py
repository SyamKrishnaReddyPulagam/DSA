class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xFFFFFFFF
        while b:
            z=(a&b)<<1
            a=(a^b)&mask
            b=z&mask
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)