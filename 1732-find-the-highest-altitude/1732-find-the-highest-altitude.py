class Solution(object):
    def largestAltitude(self, gain):
        a=[]
        j=0
        a.append(0)
        for i in range(len(gain)):
            a.append(a[j]+gain[i])
            j+=1
        return max(a)
        