class Solution(object):
    def plusOne(self, digits):
        x=0
        for i in range(len(digits)):
            x=x*10+digits[i]
        x=x+1
        digits = list(map(int, str(x)))
        return digits