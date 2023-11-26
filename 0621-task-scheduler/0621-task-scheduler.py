class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        arr=[-x for x in count.values()]
        heapq.heapify(arr)
        time=0
        queue=deque()
        
        while arr or queue:
            time+=1
            
            if arr:
                z=1+heapq.heappop(arr)
                if z:
                    queue.append([z,time+n])
            if queue and time==queue[0][1]:
                heapq.heappush(arr,queue.popleft()[0])
        return time