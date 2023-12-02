class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dicti1=Counter(chars)
        ans=0
        for i in words:
            dicti2=Counter(i)
            z=0
            for j in dicti2:
                if j not in dicti1 or dicti1[j]<dicti2[j]:
                    z+=1
            if z==0:
                ans+=len(i)
        return ans