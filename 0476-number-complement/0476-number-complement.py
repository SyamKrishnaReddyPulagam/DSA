class Solution(object):
    def findComplement(self, num):
        num=bin(num).replace("0b","")
        complement=""
        for i in num:
            if i is "0":
                complement+="1"
            else:
                complement+="0"
                
        return int(complement,2)