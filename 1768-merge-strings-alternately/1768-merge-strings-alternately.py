class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=min(len(word1),len(word2))
        s=""
        for i in range(a):
            s+=word1[i]+word2[i]
        return s+word1[a:]+word2[a:]