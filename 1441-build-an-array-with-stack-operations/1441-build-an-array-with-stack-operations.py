class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        i=1
        x=target[-1]
        while target and i<=x:
            if target[0]==i:
                ans.append("Push")
                target.pop(0)
            else:
                ans.append("Push")
                ans.append("Pop")
            i+=1
        return ans