class Solution(object):
    def totalMoney(self, n):
        weeks,days=n//7,n%7
        monday=weeks+1
        ans=0
        if weeks>0:
            ans+=((weeks)*(2*28+(weeks-1)*7))/2
        if days>=1:
            ans+=(days*(2*monday+(days-1)))/2
        return ans