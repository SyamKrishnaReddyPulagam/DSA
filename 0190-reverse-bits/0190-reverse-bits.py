class Solution:
    def reverseBits(self, n):
        n=bin(n).replace("0b","")
        n=str(n)
        x=32-len(n)
        y=""
        for i in range(x):
            y+='0'
        n=y+n
        n=n[::-1]
        return int(n,2)