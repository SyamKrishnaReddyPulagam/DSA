class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dicti={i:0 for i in [5,10,20]}
        for i in bills:
            if i!=5:
                if i==10:
                    if dicti[5]<1: return False
                    else:
                        dicti[5]-=1
                else:
                    if dicti[10]<1:
                        if dicti[5]>=3:
                            dicti[5]-=3
                        else:
                            return False
                    else:
                        if dicti[5]>=1:
                            dicti[10]-=1
                            dicti[5]-=1
                        else:
                            return False
            dicti[i]+=1
        return True