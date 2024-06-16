class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        for i in range(len(hours)):
            hours[i]=hours[i]%24
        ans=0
        for i in range(len(hours)):
            for j in range(i+1,len(hours)):
                if hours[i]+hours[j]==24 or hours[i]+hours[j]==0:
                    ans+=1
        return ans