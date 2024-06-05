class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n=len(words)
        if n==1:
            return list(words[0])
        dicti=Counter(words[0])
        for i in range(1,len(words)):
            dicti &=Counter(words[i])
        return list(dicti.elements())