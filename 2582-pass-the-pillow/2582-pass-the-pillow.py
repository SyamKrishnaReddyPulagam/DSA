class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        ind,front,back=1,True,False
        while True:
            time-=1
            if front:
                ind+=1
                if ind==n:
                    front=False
                    back=True
            elif back:
                ind-=1
                if ind==1:
                    front=True
                    back=False
            if time==0:
                return ind
            
                    