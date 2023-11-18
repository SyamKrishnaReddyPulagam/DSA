class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        n=len(sentences)
        ans=0
        for i in range(n):
            z=sentences[i].split(" ")
            ans=max(ans,len(z))
            print(ans,len(z))
        return ans