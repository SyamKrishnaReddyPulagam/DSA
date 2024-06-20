class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if m*k>n:
            return -1
        elif m*k==n:
            return max(bloomDay)
        def func(temp,day,m,k):
            streak=0
            count=0
            for i in temp:
                if i<=day:
                    streak+=1
                else:
                    streak=0
                if streak==k:
                    count+=1
                    streak=0
            if count>=m:
                return True
            return False
        left,right=1,max(bloomDay)
        ans=float("inf")
        while left<=right:
            mid=(left+right)//2
            if func(bloomDay,mid,m,k):
                ans=min(ans,mid)
                right=mid-1
            else:
                left=mid+1
        return ans