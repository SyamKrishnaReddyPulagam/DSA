class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #words.sort(reverse=True)
        dicti=Counter(words)
        ans=[]
        for i in dicti.keys():
            ans.append([dicti[i],i])
        ans.sort(key=lambda x:(-x[0],x[1]))
        ans=ans[:k]
        z=[]
        for i in ans:
            z.append(i[1])
        return z