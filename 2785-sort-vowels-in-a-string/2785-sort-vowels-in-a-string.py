class Solution:
    def sortVowels(self, s: str) -> str:
        dicti={"A","E","I","O","U","a","e","i","o","u"}
        vowels=[]
        index=[]
        s=list(s)
        n=len(s)
        for i in range(n):
            if s[i] in dicti:
                vowels.append(s[i])
                index.append(i)
        vowels.sort()
        z=0
        for i in index:
            s[i]=vowels[z]
            z+=1
        return "".join(s)