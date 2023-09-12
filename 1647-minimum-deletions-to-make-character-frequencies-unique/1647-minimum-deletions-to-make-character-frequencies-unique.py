class Solution:
    def minDeletions(self, s: str) -> int:
        x=collections.Counter(s)
        y=set()
        n_op=0
        for val,freq in x.items():
            while freq>0 and freq in y:
                freq-=1
                n_op+=1
            y.add(freq)
        print(x,y)
        return n_op