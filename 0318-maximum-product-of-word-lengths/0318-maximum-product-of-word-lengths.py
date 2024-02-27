class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def func(a,b):
            a=list(set(a))
            b=list(set(b))
            temp=[]
            for i in a:
                if i in b:
                    temp.append(i)
            return len(temp)==0
        ans=float("-inf")
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if func(words[i],words[j]):
                    ans=max(ans,len(words[i])*len(words[j]))
        if ans==float("-inf"):
            return 0
        return ans