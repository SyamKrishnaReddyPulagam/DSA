class Solution(object):
    def kthDistinct(self, arr, k):
        dicti=defaultdict(int)
        for i in arr:
            dicti[i]+=1
        for i in arr:
            if dicti[i]==1:
                k-=1
            if k==0:
                return i
        return ""
            