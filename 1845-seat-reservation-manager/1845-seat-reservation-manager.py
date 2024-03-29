class SeatManager(object):

    def __init__(self, n):
        self.arr=list(range(1, n+1))

        heapq.heapify(self.arr)

    def reserve(self):
        reserved=heapq.heappop(self.arr)
        return reserved
        

    def unreserve(self, seatNumber):
        heapq.heappush(self.arr,seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)