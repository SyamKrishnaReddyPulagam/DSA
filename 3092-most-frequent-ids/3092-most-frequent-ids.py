class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        dicti={}
        n,heap=len(nums),[]
        ans=[0]*n
        for i,(ele,fre) in enumerate(zip(nums,freq)):
            if ele not in dicti:
                dicti[ele]=fre
            else:
                dicti[ele]+=fre
            heapq.heappush(heap,[-dicti[ele],ele])
            while heap and -heap[0][0]!=dicti[heap[0][1]]: 
                """top elements which are not updated are being removed and for that we use dicti to check. this step help us to update the fre of element without actually updating i.e by removing the previous frequency count of element when it in top else it will not bother us anyway"""
                heapq.heappop(heap)
            if heap:
                ans[i]=-heap[0][0]
        return ans
            