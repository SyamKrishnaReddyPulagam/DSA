class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)==2:
            return skill[0]*skill[1]
        
        tot=sum(skill)
        np=len(skill)//2
        if tot%np!=0:
            return -1
        k=tot//np
        x=0
        sums=0
        pair = defaultdict(int)
        for n in skill:
            if n>k:
                return -1
            if pair[k-n]!=0:
                pair[k-n]-=1
                sums+=n*(k-n)
                x+=1
            else: 
                pair[n] += 1
        if x==len(skill)//2:
            return sums
        return -1