class FreqStack:

    def __init__(self):
        self.dicti1={}
        self.dicti2={}
        self.maxcount=0
        
    def push(self, val: int) -> None:
        if val in self.dicti2:
            self.dicti2[val]+=1
        else:
            self.dicti2[val]=1
        z=self.dicti2[val]
        if z in self.dicti1:
            self.dicti1[z].append(val)
        else:
            self.dicti1[z]=[val]
        if z>self.maxcount:
            self.maxcount=z

    def pop(self) -> int:
        a=self.dicti1[self.maxcount].pop()
        self.dicti2[a]-=1
        if not self.dicti1[self.maxcount]:
            self.maxcount-=1
        return a


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()