class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        nums=sentence.split()
        ans=[]
        maxlen=0
        for i in dictionary:
            maxlen=max(maxlen,len(i))
        for word in nums:
            n,i,bol=len(word),0,False
            while i<n:
                if word[:i+1] in dictionary:
                    ans.append(word[:i+1])
                    bol=True
                    break
                i+=1
            if not bol:
                ans.append(word)
        return " ".join(ans)