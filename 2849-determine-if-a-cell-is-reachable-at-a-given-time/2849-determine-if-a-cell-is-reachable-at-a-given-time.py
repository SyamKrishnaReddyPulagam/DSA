class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        xdiff=abs(fx-sx)
        ydiff=abs(fy-sy)
        
        if xdiff==0 and ydiff==0 and t==1:
            return False
        return max(xdiff,ydiff)<=t