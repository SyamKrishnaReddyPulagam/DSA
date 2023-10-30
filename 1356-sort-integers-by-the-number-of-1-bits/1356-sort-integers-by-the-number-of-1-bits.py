class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        dicti={}
        arr.sort()
        for i in arr:
            z=bin(i).count("1")
            if z in dicti:
                dicti[z].append(i)
            else:
                dicti[z]=[i]
        sorted_dicti= sorted(dicti.items(), key=lambda x:x[0])
        ans=[]
        for i in sorted_dicti:
            ans+=i[1]
        return ans