class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=min(len(word1),len(word2))
        s=""
        for i in range(a):
            s+=word1[i]
            s+=word2[i]
        word1=word1[a:]
        word2=word2[a:]
        if len(word1)!=0:
            s=s+word1
        if len(word2)!=0:
            s=s+word2
        return s