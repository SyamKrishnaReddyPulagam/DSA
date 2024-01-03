class RecentCounter:

    def __init__(self):
        self.arr=[]

    def ping(self, t: int) -> int:
        self.arr.append(t)
        z=t-3000
        i=0
        while i<len(self.arr):
            if self.arr[i]<z:
                i+=1
            else:
                break
        self.arr=self.arr[i:]
        return len(self.arr)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)