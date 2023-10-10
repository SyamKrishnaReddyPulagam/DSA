class SmallestInfiniteSet:

    def __init__(self):
        import numpy as np
        self.arr=np.arange(1,1001,1)
        self.arr=list(self.arr)
        heapq.heapify(self.arr)
        
    def popSmallest(self) -> int:
        return heapq.heappop(self.arr)
    def addBack(self, num: int) -> None:
        if num not in self.arr:
            heapq.heappush(self.arr,num)
        
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)