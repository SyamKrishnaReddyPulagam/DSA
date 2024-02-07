class Solution:
    def frequencySort(self, s: str) -> str:
        dicti=Counter(s)
        ans=[]
        for i in dicti:
            ans.append([i,dicti[i]])
        ans.sort(key=lambda x:-x[1])
        s=""
        for i in ans:
            s+=i[0]*i[1]
        return s