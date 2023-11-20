class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans=0
        n=len(garbage)
        cache=sum(travel)
        for char in "MGP":
            temp=0
            last=-1
            for i in range(n):
                if i>0:
                    temp+=travel[i-1]
                if char in garbage[i]:
                    last=i
                    temp+=garbage[i].count(char)
            if last<n-1:
                c=travel[last:]
                temp-=sum(c)
            if last!=-1:
                ans+=temp
        return ans