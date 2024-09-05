class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sn=mean*(len(rolls)+n)-sum(rolls)
        ele=[int(sn/n)]*n
        print(sn,ele)
        if sn>6*n or sn<=0:
            return []
        if sn%n==0:
            return ele
        else:
            for i in range(sn%n):
                ele[i]+=1
        return ele