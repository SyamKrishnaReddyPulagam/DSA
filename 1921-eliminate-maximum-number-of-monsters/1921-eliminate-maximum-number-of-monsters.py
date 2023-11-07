class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time=[]
        import math
        n=len(dist)
        for i in range(n):
            z=math.ceil(dist[i] / speed[i])
            #z=round(z,2)
            time.append(z)
        time.sort()
        count=0
        i=0
        print(time)
        while i<n:
            if i>=time[i]:
                return count
            count+=1
            i+=1
        return count
        