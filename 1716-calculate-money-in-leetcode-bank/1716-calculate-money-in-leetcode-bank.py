class Solution(object):
    def totalMoney(self, n):
        weeks,days=n//7,n%7
        monday=1
        ans=0
        while weeks>=1:
            ans+=(7*(2*monday+6))/2
            monday+=1
            weeks-=1
        if days>=1:
            ans+=(days*(2*monday+(days-1)))/2
        return ans