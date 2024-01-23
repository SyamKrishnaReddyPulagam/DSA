class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n=len(arr)
        temp=[""]
        ans=0
        for i in arr:
            cache=[]
            for j in temp:
                if len(set(i+j))!=len(i+j):
                    continue
                cache.append(i+j)
                ans=max(ans,len(i+j))
            if cache:
                temp=temp+cache
        return ans