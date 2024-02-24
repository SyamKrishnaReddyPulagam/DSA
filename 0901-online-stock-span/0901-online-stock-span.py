class StockSpanner:

    def __init__(self):
        self.arr=[]
        self.stack=[]
        self.ans=[]

    def next(self, price: int) -> int:
        if not self.arr:
            self.arr.append(price)
            self.stack.append(0)
            self.ans.append(1)
            return 1
        else:
            self.arr.append(price)
            while self.stack and self.arr[self.stack[-1]]<=price:
                self.stack.pop()
            if self.stack:
                self.ans.append((len(self.arr)-1)-self.stack[-1])
            else:
                self.ans.append(len(self.arr))
            self.stack.append(len(self.arr)-1)
            return self.ans[-1]
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)