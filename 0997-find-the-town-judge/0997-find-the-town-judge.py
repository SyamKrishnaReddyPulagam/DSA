class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dicti={}
        for i in range(1,n+1):
            dicti[i]=[]
        for i in trust:
            dicti[i[0]].append(i[1])
        z=set()
        for i in dicti:
            if dicti[i]==[]:
                z.add(i)
        z=list(z)
        if len(z)!=1:
            return -1
        else:
            for i in dicti:
                if i!=z[0] and z[0] not in dicti[i]:
                    return -1
        return z[0]