class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dicti=Counter(arr)
        temp=[[dicti[i],i] for i in dicti]
        temp.sort(key=lambda x:[x[0],x[1]])
        if k<temp[0][0]:
            return len(temp)
        i=0
        while k>0 and i<len(temp):
            k-=temp[i][0]
            i+=1
        if k<0:
            return len(temp)-i+1
        return len(temp)-i