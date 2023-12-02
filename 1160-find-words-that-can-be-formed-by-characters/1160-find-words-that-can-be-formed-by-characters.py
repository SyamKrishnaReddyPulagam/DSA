class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dicti1={}
        for i in chars:
            if i in dicti1:
                dicti1[i]+=1
            else:
                dicti1[i]=1
        ans=0
        for i in words:
            dicti2={}
            for j in i:
                if j in dicti2:
                    dicti2[j]+=1
                else:
                    dicti2[j]=1
            z=0
            for j in dicti2:
                if j not in dicti1 or dicti1[j]<dicti2[j]:
                    z+=1
            if z==0:
                ans+=len(i)
        return ans