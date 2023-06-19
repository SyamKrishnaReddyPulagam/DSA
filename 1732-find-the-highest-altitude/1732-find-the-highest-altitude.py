class Solution(object):
    def largestAltitude(self, gain):
        a=[]
        j=0
        max1=float('-inf')
        a.append(0)
        for i in range(len(gain)):
            a.append(a[j]+gain[i])
            max1=max(max1,a[j]+gain[i])
            j+=1
        return max(0,max1)
        