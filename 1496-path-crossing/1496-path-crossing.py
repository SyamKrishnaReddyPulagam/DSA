class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dicti={(0,0):1}
        point=[0,0]
        n=len(path)
        for i in range(n):
            if path[i]=="N":
                point[1]+=1
            elif path[i]=="S":
                point[1]-=1
            elif path[i]=="E":
                point[0]+=1
            else:
                point[0]-=1
            x=tuple(point)
            if x in dicti:
                return True
            else:
                dicti[x]=1
        return False