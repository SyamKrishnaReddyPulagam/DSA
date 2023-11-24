class Solution:
    def findComplement(self, num: int) -> int:
        z=bin(num).replace("0b","")
        z=len(z)
        y="1"*z
        y=int(y,2)
        return num^y