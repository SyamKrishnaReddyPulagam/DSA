class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n=len(word)
        if k>n:
            return 1
        ans,s=1,word
        def func(word,s):
            for i in range(len(word)):
                if word[i]!="*" and s[i]!=word[i]:
                    return False
            return True
        word=word[k:]+"*"*k
        while not func(word,s):
            word=word[k:]+"*"*k
            ans+=1
        return ans