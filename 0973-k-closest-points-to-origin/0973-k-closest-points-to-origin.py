class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr=[]
        n=len(points)
        for i,j in points:
            dist=(i**2)+(j**2)
            arr.append([dist,i,j])
        heapq.heapify(arr)
        ans=[]
        while k>0:
            x,y,z=heapq.heappop(arr)
            ans.append([y,z])
            k-=1
        return ans