class Solution(object):
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x:x[1])
        count=1
        i=1
        j=pairs[0][1]
        while i<len(pairs):
            if pairs[i][0]>j:
                count+=1
                j=pairs[i][1]
            i+=1
        return count