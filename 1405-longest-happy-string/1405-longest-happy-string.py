class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        arr,ans=[],""
        heapq.heapify(arr)
        if a:
            heapq.heappush(arr,[-a,"a"])
        if b:
            heapq.heappush(arr,[-b,"b"])
        if c:
            heapq.heappush(arr,[-c,"c"])
        while arr:
            count,ele=heapq.heappop(arr)
            if len(ans)>=2 and ans[-2:]==ele*2:
                if not arr:
                    break
                c,e=heapq.heappop(arr)
                heapq.heappush(arr,[count,ele])
                count,ele=c,e
            print(count,ele,ans)
            ans+=ele
            count+=1
            if count<0:
                heapq.heappush(arr,[count,ele])
        return ans